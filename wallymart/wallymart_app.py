#!/usr/bin/env python3

import os
import logging
import argparse
from wallymart.utils.logger_configurator import LoggerConfigurator


class WallymartApp:
    def __init__(self, args=None):
        self._log_filename = "wallymart"
        self._args = args
        self._logger = logging.getLogger(__name__)

        self._parse_args()  # updates args
        self._configure_log()  # updates logger

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
        if args is None:
            args = self._args

        os.makedirs(args.log_dir, exist_ok=True)
        self._logger = LoggerConfigurator(
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
        """main function
        """

        # Home page
        self.log("""Welcome to Wallymart""")  # put something pretty here


        # select login or sign up
        while True:
            choice = input("Please choose: (1) sign up, (2) log in: ")
            if choice not in ('1', '2'):
                print("Please pick a valid choice")
            else:
                break

        self.log(f"Please choose: (1) sign up, (2) log in: {choice}")

        
        # module to create a customer or employee
        # module to save to flat file
        # module to display products with reviews
        # module to select a product based on the number and add it to cart
        # module to send order
        # module to write a review
        # module to add orders to a list that only employees can view


if __name__ == '__main__':
    app = WallymartApp()
    app.run()
