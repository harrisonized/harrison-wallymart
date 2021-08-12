#!/usr/bin/env python3

"""Employee pages
"""

import logging
import pandas as pd
from wallymart.database_manager.database_connection import DatabaseConnection
from wallymart.order_manager.product import Product


class EmployeePortal:
    """All methods are class methods so do not require instantiating the class
    This class is meant to be inherited by Pages
    """

    # ----------------------------------------------------------------------
    # Public

    @staticmethod
    def home(logger):

        while True:
            choice = input(
                "Please choose: "
                "(1) view delivery items, "
                "(2) add products, "
                "(3) update profile, "  # shared
                "(4) log out: "
            )
            if choice not in ('1', '2', '3', '4'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(
            "Please choose: "
            "(1) view delivery items, "
            "(2) add products, "
            "(3) update profile, "
            "(4) log out: "
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

    # ----------------------------------------------------------------------
    # TODO

    @classmethod
    def delivery_page(cls, logger=None):
        if logger is None:
            logger = cls._logger

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

        # write to database
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

        return 200
    