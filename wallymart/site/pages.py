#!/usr/bin/env python3

"""Shared pages
"""

import logging
from wallymart.credential_manager.credentials import Credentials
from .portal.customer_portal import CustomerPortal
from .portal.employee_portal import EmployeePortal


class Pages(CustomerPortal, EmployeePortal):
    def __init__(self, logger=None):
        self._logger = logger or logging.getLogger(__name__)

    # ----------------------------------------------------------------------
    # Public

    def add_logger(self, logger):
        self._logger = logger

    def home_page(self, logger=None):
        """Home page
        Need seperate login for employees
        """
        if logger is None:
            logger = self._logger

        logger.log("""Welcome to Wallymart""")  # put something pretty here
        while True:
            sign_up_or_log_in = input("Please choose: (1) sign up, (2) log in: ")
            if sign_up_or_log_in not in ('1', '2'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(f"Please choose: (1) sign up, (2) log in: {sign_up_or_log_in}")
        return sign_up_or_log_in

    def signup_page(self, logger=None):
        if logger is None:
            logger = self._logger
        username = input("Username: ")
        password = input("Password: ")
        self._credentials = Credentials(username, password)
        logger.log(
            f"username: {self._credentials.get_username()} \n" \
            f"password: {self._credentials.get_password()}"
        )

    def login_page(self, logger=None):
        if logger is None:
            logger = self._logger
        username = input("Username: ")
        password = input("Password: ")
        self._credentials = Credentials(username, password)
        logger.log(
            f"username: {self._credentials.get_username()} \n" \
            f"password: {self._credentials.get_password()}"
        )
        return True
