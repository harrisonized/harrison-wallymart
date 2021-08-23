#!/usr/bin/env python3

"""Employee pages
"""

import logging
import json
import pandas as pd
from wallymart.utils.database_connection import DatabaseConnection
from wallymart.orm.employee import Employee
from wallymart.orm.product import Product


class EmployeePortal:
    """All methods are class methods so do not require instantiating the class
    This class is meant to be inherited by Pages

    Methods:
        employee_home
            (1) view items to deliver
            (2) view products
            (3) add products
            (4) update profile
            (5) log out
        delivery_page
            (1) refresh orders view
            (2) next page
            (3) previous page
            (4) examine order
        add_products_page
        employee_profile_page
            (1) check data
            (2) update first name
            (3) update last name
            (4) save changes
            (5) exit without savin
    """

    # ----------------------------------------------------------------------
    # Public

    @staticmethod
    def home(logger):

        while True:
            choice = input(
                "Please choose: "
                "(1) view items to deliver, "
                "(2) view_products, "
                "(3) add products, "
                "(4) update profile, "
                "(5) log out: "
            )
            if choice not in ('1', '2', '3', '4', '5'):
                logger.log("Please pick a valid choice")
            else:
                break
        logger.log(
            "Please choose: "
            "(1) view items to deliver, "
            "(2) view_products, "
            "(3) add products, "
            "(4) update profile, "
            "(5) log out: "
            f"{choice}"
        )
        return choice

    # see: https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name
    __home = home  # local reference

    @classmethod
    def employee_home(cls):
        """Requires that cls._logger be used as the logger
        """
        return cls.__home(cls._logger)

    @classmethod
    def delivery_page(cls, logger=None):
        if logger is None:
            logger = cls._logger

        database_connection = DatabaseConnection(f"orders.csv")
        view = database_connection.get_view()
        logger.log(view)

        while True:

            choice = input(
                "Please choose: "
                "(1) refresh orders view, "
                "(2) next page, "
                "(3) previous page, "
                "(4) examine order, "
                "Enter empty to go back "
            )
            if choice not in ('1', '2', '3', '4'):
                break

            if choice=='1':
                view = database_connection.get_view()
                logger.log(view)

            # next page
            elif choice=='2': 
                database_connection.next_page()
                view = database_connection.get_view()
                logger.log(view)

            # previous page
            elif choice=='3':
                database_connection.prev_page()
                view = database_connection.get_view()
                logger.log(view)

            elif choice=='4':

                # get product_id
                while True:
                    order_id = input("Enter the order id: ")
                    try:
                        order_id = int(order_id)
                    except:
                        logger.log("order id should be an integer")
                    break

                table = database_connection.table
                order = table.loc[(table['order_id']==order_id), "order"][0]  # order_id should be unique
                logger.log(json.dumps(json.loads(order), indent=1))  # pretty logger.log the json


            else:
                break

    @classmethod
    def add_products_page(cls, logger=None):

        if logger is None:
            logger = cls._logger
        database_connection = DatabaseConnection(f"products.csv")
        table = database_connection.table

        product = Product()  # container

        logger.log(
            "Note: Please do not use this interface to update existing products or enter many products"
        )

        # set product name
        while True:
            logger.log("Enter 0 to exit")
            product_name = input("Product name: ")

            if product_name=="0":
                logger.log("Returning to portal")
                return 200
            elif product_name=='':
                logger.log('Please choose a valid product name')
            elif len(table[(table[f'product_name']==product_name)]) > 0:
                logger.log(f"{product_name} already exists, please enter a unique product name")
            else:
                product.set_product_name(product_name)  # to be saved
                break

        product.set_description(input("Description: "))

        # set quantity
        while True:
            quantity = input("Quantity: ")
            try:
                int(quantity)
            except ValueError:
                quantity = ""
            if quantity=="":
                logger.log('Please choose a valid integer quantity')
            else:
                product.set_quantity(int(quantity))  # to be saved
                break

        # set price
        while True:
            price = input("Price: ")
            try:
                float(price)
            except ValueError:
                price = ""
            if price=="":
                logger.log('Please choose a valid USD price, eg. $9.99 without the $')
            else:
                product.set_price(round(float(price), 2))  # to be saved
                break

        # save
        while True:
            confirm = input("Type 'yes' to confirm your new product, "
                            "Enter empty to exit without saving: ")
            if confirm == 'yes':
                last_id = table[f'product_id'].max()
                if pd.isna(last_id):
                    last_id = 0
                df = pd.DataFrame.from_records([
                    {'product_id': last_id + 1,
                     'product_name': product.get_product_name(),
                     'description': product.get_description(),
                     'quantity': product.get_quantity(),
                     'price': product.get_price(),
                    }
                ])
                database_connection.append(df)
                logger.log("Product created!")
                break

        return 200

    @classmethod
    def profile_page(cls, employee_id, logger=None):
        if logger is None:
            logger = cls._logger

        database_connection = DatabaseConnection(f"employees.csv")
        table = database_connection.table
        employee = Employee(employee_id)

        view = table[(table['employee_id']==employee.get_employee_id())]
        logger.log(view)

        while True:

            choice = input(
                "Please choose: "
                "(1) check data, "
                "(2) update first name, "
                "(3) update last name, "
                "(4) save changes, "
                "(5) exit without saving "
            )
            if choice not in ('1', '2', '3', '4', '5'):
                logger.log("Please pick a valid choice")
            elif choice=='1':
                view = table[(table['employee_id']==employee.get_employee_id())]
                logger.log(view)
            elif choice=='2':
                first_name = input("Enter your first name: ")
                employee.set_first_name(first_name)
            elif choice=='3':
                last_name = input("Enter your last name: ")
                employee.set_last_name(last_name)
            elif choice=='4':
                table[
                    (table['employee_id']==employee.get_employee_id())
                ] = pd.Series(
                    {'employee_id': employee.get_employee_id(),
                     'first_name': employee.get_first_name(),
                     'last_name': employee.get_last_name(),
                    }
                )
                database_connection.overwrite()
                logger.log("Information saved!")
            else:
                break

    __profile_page = profile_page  # local reference

    @classmethod
    def employee_profile_page(cls, employee_id):
        """Requires that cls._logger be used as the logger
        """
        return cls.__profile_page(employee_id, cls._logger)
