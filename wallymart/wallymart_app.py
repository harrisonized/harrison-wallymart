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
        self._username = ''
        self._authenticated = False
        self._customer_or_employee = None
        self._pages = Pages()
        self._shopping_cart = None

        # initialize app
        self._parse_args()
        self._configure_log()
        self._logger.add_stream_handler()
        # self._logger.add_file_handler()  # disable during testing
        self._configure_database()
        self._pages.add_logger(self._logger)

    # ----------------------------------------------------------------------
    # Private

    def _parse_args(self):
        parser = argparse.ArgumentParser(description='')
        parser.add_argument("-l", "--log-dir", dest="log_dir", default='logs', action="store",
                            required=False, help="set the directory for storing log files")
        parser.add_argument('--debug', action='store_true',
                            help='print debug messages')
        self._args = parser.parse_args()

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

    def _configure_database(self):
        """Initialize database if not exist
        """
        db_configurator = DatabaseConfigurator()
        db_configurator.initialize_database()

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
            self._customer_or_employee, signup_or_login = self._pages.home_page()
            if signup_or_login=='1':
                self._pages.signup_page(self._customer_or_employee)
            elif signup_or_login=='2':
                self._authenticated, self._username = self._pages.login_page(self._customer_or_employee)
            else:
                pass
        
        self.log(f'Logging in as {self._username}...')

        # employee portal
        if self._customer_or_employee == '2':
            while self._authenticated:
                employee_choice = self._pages.employee_home(self._username)
                if employee_choice=='1':
                    self._pages.delivery_page()
                elif employee_choice=='2':
                    self._pages.view_products_page()
                elif employee_choice=='3':
                    self._pages.add_products_page()
                elif employee_choice=='4':
                    self._pages.update_profile_page(self._username)
                elif employee_choice=='5':
                    self._authenticated = False
                    self.log(f'Logging out of {self._username}...')
                    self.log('Thank you for using Wallymart!')
                else:
                    pass

        # ----------------------------------------------------------------------
        # Employee Pages       

        # Employee Portal
        # (1): Update profile
        # (2): Add new product
        # (3): View Orders
        # (4): Update order


        # ----------------------------------------------------------------------
        # Customer Pages

        # Customer Portal
        # list products automatically (10 per page, loop)
        # Select an option:
        # (0): Log out
        # (1): Update profile
        # (2): View item -> sends to item page
        # (3): Add item to cart
        # (4): Checkout  -> sends to checkout

        # Item page (from view item option)
        # display reviews automatically (10 per page, loop)
        # Select an option: 
        # (0): Log out
        # (1): Add item to cart
        # (2): Select a review -> sends to review page
        # (2): Write a review -> sends to form
        # (3): Go back to customer portal

        # Review page
        # display full review
        # (0): Log out
        # (1): Upvote review
        # (2): Downvote review
        # (3): Go back to item page
        # (4): Go back to customer portal

        # Review form
        # enter a review
        # need logic to only add one review per customer
        # (0): Log out
        # (1): Submit review  # overwrite existing review
        # (2): Go back to item page

        # Checkout page
        # add cart to orders table
        # (1): Add credit card info
        # (2): Add shipping address
        # (3): Submit order -> return to customer portal



        

if __name__ == '__main__':
    app = WallymartApp()
    app.run()
