#!/usr/bin/env python3

"""Shared pages
"""

import logging
import pandas as pd
from wallymart.database_manager.database_connection import DatabaseConnection
from wallymart.credential_manager.credentials import Credentials
from .portal.customer_portal import CustomerPortal
from .portal.employee_portal import EmployeePortal


class Pages(CustomerPortal, EmployeePortal):
    """All methods are class methods so do not require instantiating the class
    """
    _logger = logging.getLogger(__name__)

    # ----------------------------------------------------------------------
    # Public

    @classmethod
    def add_logger(cls, logger):
        """Save Wallymart._logger to the class
        """
        cls._logger = logger

    @classmethod
    def home(cls, logger=None):
        """Home page
        """
        if logger is None:
            logger = cls._logger

        logger.log("""Welcome to Wallymart""")  # put something pretty here

        while True:
            customer_or_employee = input("Are you a: (1) customer or (2) employee? ")
            if customer_or_employee not in ('1', '2'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(f"Are you a: (1) customer or (2) employee? {customer_or_employee}")

        while True:
            signup_or_login = input("Please choose: (1) create account, (2) log in: ")
            if signup_or_login not in ('1', '2'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(f"Please choose: (1) create account, (2) log in: {signup_or_login}")
        return customer_or_employee, signup_or_login

    @classmethod
    def signup_page(cls, customer_or_employee, logger=None):

        if customer_or_employee=='1':
            user = 'customer'
        elif customer_or_employee=='2':
            user = 'employee'
        else:
            raise KeyError('Enter a valid option')

        if logger is None:
            logger = cls._logger
        database_connection = DatabaseConnection(f"{user}_credentials.csv")
        table = database_connection.table
        credentials = Credentials()  # container

        # set username
        while True:
            logger.log("Enter 0 to exit")
            username = input("Username: ")
            credentials.set_username(username)  # to be saved
            if username=="0":
                logger.log("Returning to home...")
                return 200  # OK
            elif username=='':
                logger.log('Please choose a valid username')
            elif len(table[(table[f'{user}_username']==credentials.get_username())]) > 0:
                logger.log(f"{username} already exists, please enter a unique username")
            else:
                break

        # set password
        while True:
            password = input("Password: ")
            if password=='':
                logger.log('Please choose a valid password')
            else:
                credentials.set_password(password)  # to be saved
                break

        # user feedback
        # logger.log(
        #     f"username: {credentials.get_username()} \n" \
        #     f"password: {credentials.get_password()}"
        # )

        # write to database
        last_id = table[f'{user}_id'].max()
        if pd.isna(last_id):
            last_id = 0
        df = pd.DataFrame.from_records([
            {f'{user}_id': last_id + 1,
             f'{user}_username': credentials.get_username(),
             f'{user}_password': credentials.get_password(),
            }
        ])
        database_connection.append(df)
        logger.log("User created!")

        return 200  # OK

    @classmethod
    def login_page(cls, customer_or_employee, logger=None):

        if customer_or_employee=='1':
            user = 'customer'
        elif customer_or_employee=='2':
            user = 'employee'
        else:
            raise KeyError('Enter a valid option')

        if logger is None:
            logger = cls._logger
        database_connection = DatabaseConnection(f"{user}_credentials.csv")
        table = database_connection.table
        _authenticated = False

        while True:
            logger.log("Enter empty to exit")
            username = input("Username: ")
            password = input("Password: ")
            if username=='' and password=='':
                logger.log('Returning to home...')
                return _authenticated, username
            credentials = Credentials(username, password)
            if len(table[(table[f'{user}_username']==credentials.get_username())
                      & (table[f'{user}_password']==credentials.get_password())]) >= 1:
                _authenticated = True
                logger.log("Logged in!")
                break
            else:
                logger.log("Please enter a valid username and password combination")

        return _authenticated, username

    @classmethod
    def update_profile_page(cls, username, logger=None):
        if logger is None:
            logger = cls._logger
