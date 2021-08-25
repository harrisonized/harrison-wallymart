#!/usr/bin/env python3

"""Shared pages
"""

import logging
import pandas as pd
from wallymart.utils.database_connection import DatabaseConnection
from wallymart.orm.credentials import Credentials
from wallymart.orm.customer import Customer
from wallymart.orm.employee import Employee
from wallymart.orm.order_item import OrderItem
from wallymart.orm.review import Review
from .portal.customer_portal import CustomerPortal
from .portal.employee_portal import EmployeePortal


class Pages(CustomerPortal, EmployeePortal):
    """All methods are class methods so do not require instantiating the class

    Methods:
        add_logger
        home
        signup_page
        login_page
        view_products
            (1) refresh products view
            (2) next page
            (3) previous page
            (4) add item to cart
            (5) write a review
            (6) view reviews
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
                logger.log("Please pick a valid choice")
            else:
                break
        logger.log(f"Are you a: (1) customer or (2) employee? {customer_or_employee}")

        while True:
            signup_or_login = input("Please choose: (1) create account, (2) log in: ")
            if signup_or_login not in ('1', '2'):
                logger.log("Please pick a valid choice")
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
                credentials.set_user_id(df[f'{user}_id'].iloc[0])
                authenticated = True
                return credentials, True

    @classmethod
    def products_page(cls, shopping_cart, customer_or_employee, logger=None):

        if logger is None:
            logger = cls._logger

        database_connection = DatabaseConnection(f"products.csv")
        view = database_connection.get_view()
        logger.log(view)

        while True:

            if customer_or_employee=='1':
                choice = input(
                    "Please choose: "
                    "(1) refresh products view, "
                    "(2) next page, "
                    "(3) previous page, "
                    "(4) add item to cart, "
                    "(5) write a review, "
                    "(6) view reviews, "
                    "Enter empty to go back "
                )
                if choice not in ('1', '2', '3', '4', '5', '6'):
                    break

            # limit choices for employees
            else:  # customer_or_employee=='2':
                choice = input(
                    "Please choose: "
                    "(1) refresh products view, "
                    "(2) next page, "
                    "(3) previous page, "
                    "Enter empty to go back "
                )
                if choice not in ('1', '2', '3'):
                    break

            if choice=='1':
                view = database_connection.get_view()
                logger.log(view)

            elif choice=='2':  # next page
                database_connection.next_page()
                view = database_connection.get_view()
                logger.log(view)

            elif choice=='3':  # previous page
                database_connection.prev_page()
                view = database_connection.get_view()
                logger.log(view)

             # add item to cart
            elif choice=='4':

                order_item = OrderItem()

                # enter product_id
                while True:
                    product_id = input("Enter the product id: ")
                    try:
                        product_id = int(product_id)
                    except:
                        logger.log("product id should be an integer")
                    order_item.set_product_id(product_id)
                    break

                # enter quantity
                while True:
                    quantity = input("Enter quantity: ")
                    try:
                        quantity = int(quantity)
                    except:
                        logger.log("quantity should be an integer")
                    order_item.set_quantity(quantity)
                    break

                shopping_cart.append(order_item)

            elif choice=='5':

                review = Review()

                # get product_id
                while True:
                    product_id = input("Enter the product id: ")
                    try:
                        product_id = int(product_id)
                    except:
                        logger.log("product id should be an integer")
                    review.set_product_id(product_id)
                    break

                # enter review
                while True:
                    review_text = input("Enter your review: ")
                    review.set_review_text(review_text)
                    break

                # save review
                while True:
                    confirm = input("Type 'yes' to confirm your review, "
                                    "Enter empty to exit without saving: ")
                    if confirm == 'yes':

                        # save order to orders table
                        review_db = DatabaseConnection(f"reviews.csv")
                        last_id = review_db.table['review_id'].max()
                        if pd.isna(last_id):
                            last_id = 0
                        df = pd.DataFrame.from_records([
                            {'review_id': last_id + 1,
                             'customer_id': shopping_cart.get_customer_id(),
                             'product_id': review.get_product_id(),
                             'review_text': review.get_review_text()
                            }
                        ])
                        review_db.append(df)

                    break

            elif choice=='6':

                # get product_id
                while True:
                    product_id = input("Enter the product id: ")
                    try:
                        product_id = int(product_id)
                    except:
                        logger.log("product id should be an integer")
                    break

                # need to come back and make this pretty
                review_db = DatabaseConnection(f"reviews.csv")
                table = review_db.table
                view = table.loc[
                            (table['product_id']==product_id),
                            ['customer_id', 'review_text']
                        ]
                if not view.empty:
                    logger.log(view)
                else:
                    logger.log("No reviews yet. Please consider writing one. ")

            else:
                break
