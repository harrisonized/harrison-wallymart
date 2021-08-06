#!/usr/bin/env python3

import os
import logging
import argparse
from wallymart.utils.logger_configurator import LoggerConfigurator


class WallymartApp:
    def __init__(self, args=None):
        self.args = args
        self.logger = logging.getLogger(__name__)
        self.script_name = "wallymart"
        self.parse_args()
        self.configure_log()

    def parse_args(self):
        parser = argparse.ArgumentParser(description='')
        parser.add_argument("-l", "--log-dir", dest="log_dir", default='logs', action="store",
                            required=False, help="set the directory for storing log files")
        parser.add_argument('--debug', action='store_true',
                            help='print debug messages')
        self.args = parser.parse_args()

    def configure_log(self, args=None):
        if args is None:
            args = self.args

        os.makedirs(args.log_dir, exist_ok=True)
        self.logger = LoggerConfigurator(
            filename=f'{args.log_dir}/{self.script_name}',
            level=logging.DEBUG if args.debug else logging.INFO
        )

    def run(self):
        """main function
        """
        self.logger.log('msg')

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
