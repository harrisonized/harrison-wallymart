#!/usr/bin/env python3

"""Entry point for the command-line application
"""

import os
import logging
import argparse

from wallymart.startup.logger_configurator import LoggerConfigurator
from wallymart.startup.database_configurator import DatabaseConfigurator
from wallymart.orm.credentials import Credentials
from wallymart.orm.order_item import OrderItem
from wallymart.utils.shopping_cart import ShoppingCart
from wallymart.site.pages import Pages


class WallymartApp:
    """The :class:`WallymartApp` object controls the execution of the program.
    As the central object or controller, the WallymartApp instantiates the
    database and the logger and is responsible for storing the :class:`wallymart.orm.credentials.Credentials`
    and the :class:`wallymart.utils.shopping_cart.ShoppingCart`.

    It calls upon the :class:`wallymart.site.pages.Pages` class, which controls subprograms within
    each block. In the first phase, the user is prompted to choose whether to create
    an account or log in as a customer or employee. After authenticating, if the
    user is a :class:`wallymart.orm.customer.Customer`, he will be prompted to navigate through the :class:`wallymart.site.portal.customer_portal.CustomerPortal`
    pages. Otherwise, if the user is an :class:Employee, he will be prompted
    to navigate through the :class:`wallymart.site.portal.employee_portal.EmployeePortal` pages.

    :ivar logging.Logger _logger: Stores an instance of the Logger class. This is used throughout \
    the execution of the program.
    :ivar str _customer_or_employeer: Stores '1' for customer, '2' for employee. This \
    controls which loop the user enters after logging in.
    :ivar Credentials _credentials: Stores an instance of the :class:`wallymart.orm.credentials.Credentials` after the \
    user authenticates.
    :ivar bool _authenticated: After authenticating is set to true. Logging out will set \
    this to False, which exits the program loops.
    :ivar _shopping_cart: Stores an instance of the :class:`ShoppingCart`
    """
    def __init__(self, args=None, logger=None):
        self._log_filename = "wallymart"
        self._args = args
        self._logger = logging.getLogger(__name__)

        self._customer_or_employee = None
        self._credentials = None
        self._authenticated = False
        self._shopping_cart = ShoppingCart()

        # initialize app
        self._parse_args()
        self._configure_database()
        self._configure_log()
        self._logger.add_stream_handler()
        self._logger.add_file_handler()  # disable during testing
        Pages.add_logger(self._logger)

    # ----------------------------------------------------------------------
    # Private

    def _parse_args(self):
        parser = argparse.ArgumentParser(description='')
        parser.add_argument("-l", "--log-dir", dest="log_dir", default='logs', action="store",
                            required=False, help="set the directory for storing log files")
        parser.add_argument('--debug', action='store_true',
                            help='print debug messages')
        self._args = parser.parse_args()

    def _configure_database(self):
        """Initialize database if not exist
        """
        db_configurator = DatabaseConfigurator()
        db_configurator.initialize_database()

    def _configure_log(self, args=None):
        """Adds the following:
        1. stream_handler to print messagese to console
        2. file_handler to save session in a log
        """
        if args is None:
            args = self._args
        self._logger = LoggerConfigurator(
            logger = self._logger,
            filename=f'{args.log_dir}/{self._log_filename}',
            level=logging.DEBUG if args.debug else logging.INFO
        )

    # ----------------------------------------------------------------------
    # Public

    def log(self, msg, level=None):
        """This is a convenience function that displays the messages in the console.
        """
        self._logger.log(msg, level)

    def run(self):
        """Execute the program.

        | For troubleshooting, use the following to skip to the desired location:
        | Be sure to set the credentials first

        | Skip login for customer:
        | >>> self._customer_or_employee = '1'
        | >>> self._authenticated = True  # use for testing
        | >>> self._credentials = Credentials('harrison', 'password')
        | >>> self._credentials.set_user_id(1)

        | Go directly to checkout as a customer:
        | >>> self._shopping_cart = ShoppingCart([OrderItem(1, 2), OrderItem(2, 3)])
        | >>> self._shopping_cart.set_customer_id(1)

        | Skip login for employee:
        | >>> self._customer_or_employee = '2'
        | >>> self._authenticated = True  # use for testing
        | >>> self._credentials = Credentials('harrison', 'password')
        | >>> self._credentials.set_user_id(1)
        """

        while not self._authenticated:
            self._customer_or_employee, signup_or_login = Pages.home()
            if signup_or_login=='1':
                Pages.signup_page(self._customer_or_employee)
            elif signup_or_login=='2':
                self._credentials, self._authenticated = Pages.login_page(self._customer_or_employee)
            else:
                pass
        
        self.log(f'Logging in as {self._credentials.get_username()}...')

        # customer portal
        if self._customer_or_employee == '1':
            self._shopping_cart.set_customer_id(self._credentials.get_user_id())
            while self._authenticated:
                customer_choice = Pages.customer_home()

                if customer_choice=='1':
                    Pages.products_page(self._shopping_cart, self._customer_or_employee)
                elif customer_choice=='2':
                    Pages.checkout_page(self._shopping_cart)
                elif customer_choice=='3':
                    Pages.customer_profile_page(
                        customer_id=self._credentials.get_user_id()
                    )
                elif customer_choice=='4':
                    self._authenticated = False
                else:
                    pass

        # employee portal
        elif self._customer_or_employee == '2':
            while self._authenticated:
                employee_choice = Pages.employee_home()
                if employee_choice=='1':
                    Pages.delivery_page()
                elif employee_choice=='2':
                    Pages.products_page(None, self._customer_or_employee)
                elif employee_choice=='3':
                    Pages.add_products_page()
                elif employee_choice=='4':
                    Pages.employee_profile_page(
                        employee_id=self._credentials.get_user_id()
                    )
                elif employee_choice=='5':
                    self._authenticated = False
                else:
                    pass

        self.log(f'Logging out of {self._credentials.get_username()}...')
        self.log('Thank you for using Wallymart!')


if __name__ == '__main__':
    app = WallymartApp()
    app.run()
