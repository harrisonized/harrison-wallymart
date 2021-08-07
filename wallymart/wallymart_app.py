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
    def __init__(self, args=None):
        self._log_filename = "wallymart"
        self._args = args
        self._logger = logging.getLogger(__name__)
        self._credentials = None
        self._authenticated = False
        self._pages = Pages()

        # initialize app
        self._parse_args()
        self._configure_log()
        self._logger.add_stream_handler()
        # self._logger.add_file_handler()  # disable during testing
        self._configure_database()

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

        os.makedirs(args.log_dir, exist_ok=True)
        self._logger = LoggerConfigurator(
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
        """main function
        """

        # sign up or log in
        while not self._authenticated:
            sign_up_or_log_in = self._pages.home_page(self._logger)
            if sign_up_or_log_in=='1':
                self._pages.signup_page(self._logger)
                self.log("User created!")
            if sign_up_or_log_in=='2':
                self._authenticated = self._pages.login_page(self._logger)

        self.log("Logged in!")

        

        # miscellaneous
        # module to create a customer or employee
        # module to display products with reviews
        # module to select a product based on the number and add it to cart
        # module to send order
        # module to write a review
        # module to add orders to a list that only employees can view


if __name__ == '__main__':
    app = WallymartApp()
    app.run()
