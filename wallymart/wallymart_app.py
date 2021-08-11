#!/usr/bin/env python3

"""Entry point for command-line application
"""

import os
import logging
import argparse

from wallymart.log_manager.logger_configurator import LoggerConfigurator
from wallymart.database_manager.database_configurator import DatabaseConfigurator
from wallymart.credential_manager.credentials import Credentials
from wallymart.site.pages import Pages


class WallymartApp:
    def __init__(self, args=None, logger=None):
        self._log_filename = "wallymart"
        self._args = args
        self._logger = logging.getLogger(__name__)
        self._customer_or_employee = None
        self._username = ''
        self._authenticated = False
        self._shopping_cart = None

        # initialize app
        self._parse_args()
        self._configure_database()
        self._configure_log()
        self._logger.add_stream_handler()
        # self._logger.add_file_handler()  # disable during testing
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
        """Add:
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
        """Convenience function
        """
        self._logger.log(msg, level)

    def run(self):
        """main
        """

        # Log in
        while not self._authenticated:
            self._customer_or_employee, signup_or_login = Pages.home_page()
            if signup_or_login=='1':
                Pages.signup_page(self._customer_or_employee)
            elif signup_or_login=='2':
                self._authenticated, self._username = Pages.login_page(self._customer_or_employee)
            else:
                pass
        
        self.log(f'Logging in as {self._username}...')

        # customer portal
        if self._customer_or_employee == '1':
            while self._authenticated:
                customer_choice = Pages.customer_home(self._username)
                if customer_choice=='1':
                    # Pages.view_products()
                    pass
                elif customer_choice=='2':
                    # Pages.view_specific_item()
                    pass
                elif customer_choice=='3':
                    # add item to cart
                    pass
                elif customer_choice=='4':
                    Pages.review_item_page(self._username)
                elif customer_choice=='5':
                    Pages.shopping_cart_page(self._username)
                elif customer_choice=='6':
                    Pages.update_profile_page(self._username)
                elif customer_choice=='7':
                    self._authenticated = False
                else:
                    pass

        # employee portal
        elif self._customer_or_employee == '2':
            while self._authenticated:
                employee_choice = Pages.employee_home(self._username)
                if employee_choice=='1':
                    Pages.delivery_page()
                elif employee_choice=='2':
                    # Pages.view_products()
                    pass
                elif employee_choice=='3':
                    # Pages.view_specific_item()
                    pass
                elif employee_choice=='4':
                    Pages.add_products_page()
                elif employee_choice=='5':
                    Pages.update_profile_page(self._username)
                elif employee_choice=='6':
                    self._authenticated = False
                else:
                    pass

        self.log(f'Logging out of {self._username}...')
        self.log('Thank you for using Wallymart!')


if __name__ == '__main__':
    app = WallymartApp()
    app.run()
