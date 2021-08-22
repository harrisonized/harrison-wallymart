#!/usr/bin/env python3

"""Shared pages
"""

import logging
import pandas as pd
from wallymart.database_manager.database_connection import DatabaseConnection
from wallymart.credential_manager.credentials import Credentials
from wallymart.credential_manager.customer import Customer
from wallymart.credential_manager.employee import Employee
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
                return
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
        user_id = last_id + 1
        df = pd.DataFrame.from_records([
            {f'{user}_id': user_id,
             f'{user}_username': credentials.get_username(),
             f'{user}_password': credentials.get_password(),
            }
        ])
        database_connection.append(df)
        logger.log("User created!")

        # add user to other table
        database_connection = DatabaseConnection(f"{user}s.csv")
        table = database_connection.table
        df = pd.DataFrame.from_records([
            {f'{user}_id': user_id}
        ])
        database_connection.append(df)

        return

    @classmethod
    def login_page(cls, customer_or_employee, logger=None):
        """Returns credentials, authenticated
        """

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

        while True:
            logger.log("Enter empty to exit")
            username = input("Username: ")
            password = input("Password: ")

            # exit
            if username=='' and password=='':
                logger.log('Returning to home...')
                return Credentials(), False

            credentials = Credentials(username, password)
            df = table[(table[f'{user}_username']==credentials.get_username())
                       & (table[f'{user}_password']==credentials.get_password())]
            if len(df) == 0:
                logger.log("Please enter a valid username and password combination")
            else:
                logger.log("Logged in!")
                credentials.set_customer_id(df['{user}_id'].iloc[0])
                authenticated = True
                return credentials, True
