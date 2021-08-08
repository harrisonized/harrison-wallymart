#!/usr/bin/env python3

"""Shared pages
"""

import logging
import pandas as pd
from wallymart.credential_manager.credentials import Credentials
from wallymart.database_manager.database_connection import DatabaseConnection
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
            response = input("Please choose: (1) sign up, (2) log in: ")
            if response not in ('1', '2'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(f"Please choose: (1) sign up, (2) log in: {response}")
        return response

    def signup_page(self, logger=None):

        # boilerplate
        if logger is None:
            logger = self._logger
        credentials = Credentials()
        database_connection = DatabaseConnection("credentials.csv")
        table = database_connection.table

        # set username
        new_username = False
        while not new_username:
            logger.log("Enter 0 to exit")
            username = input("Username: ")
            credentials.set_username(username)
            if username=="0":
                logger.log("exit")
                break
            elif username=='':
                logger.log('Please choose a valid username')
            elif len(table[(table['customer_username']==credentials.get_username())]) > 0:
                logger.log(f"Username {username} already exists, please pick a unique username")
            else:
                new_username = True

        # set password
        if new_username:
            while True:
                password = input("Password: ")
                if password=='':
                    logger.log('Please choose a valid password')
                else:
                    credentials.set_password(password)
                    logger.log(
                        f"username: {credentials.get_username()} \n" \
                        f"password: {credentials.get_password()}"
                    )
                    break

        # write to database
        last_customer_id = table.customer_id.max()
        if pd.isna(last_customer_id):
            last_customer_id = 0
        df = pd.DataFrame.from_records([
            {'customer_id': last_customer_id + 1,
             'customer_username': credentials.get_username(),
             'customer_password': credentials.get_password(),
            }
        ])
        database_connection.append(df)
        logger.log("User created!")

        return 200

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
