#!/usr/bin/env python3

"""Customer pages
"""

import logging
from wallymart.order_manager.order_item import OrderItem
from wallymart.database_manager.database_connection import DatabaseConnection

class CustomerPortal:
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
                "(1) view products, "
                "(2) checkout, "
                "(3) review item, "
                "(4) update profile, "
                "(5) log out: "
            )
            if choice not in ('1', '2', '3', '4', '5'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(
            "Please choose: "
            "(1) view products, "
            "(2) checkout, "
            "(3) review item, "
            "(4) update profile, "
            "(5) log out: "
            f"{choice}"
        )
        return choice

    # see: https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name
    __home = home  # local reference

    @classmethod
    def customer_home(cls):
        """Requires that cls._logger be used as the logger
        """
        return cls.__home(cls._logger)

    @classmethod
    def view_products(cls, shopping_cart, logger=None):
        """Should probably be handled through DatabaseConnection
        """
        if logger is None:
            logger = cls._logger
        database_connection = DatabaseConnection(f"products.csv")

        while True:

            view = database_connection.get_view()
            print(view)

            choice = input(
                "Please choose: "
                "(1) next page, "
                "(2) previous page, "
                "(3) add item to cart, "
                "(4) write a review, "
                "Any other key to exit "
            )
            if choice not in ('1', '2', '3', '4'):
                break

            if choice=='1':  # next page
                database_connection.next_page()
            elif choice=='2':  # previous page
                database_connection.prev_page()
            elif choice=='3':  # add item to cart
                order_item = OrderItem()

                # get product_id
                while True:
                    product_id = input("Enter the product_id: ")
                    try:
                        product_id = int(product_id)
                    except:
                        logger.log("product id should be an integer")
                    order_item.set_product_id(int(product_id))
                    break

                # get product_id
                while True:
                    quantity = input("Enter quantity: ")
                    try:
                        quantity = int(quantity)
                    except:
                        logger.log("quantity should be an integer")
                    order_item.set_quantity(quantity)
                    break

                shopping_cart.append(order_item)
                # enter logic to add this to cart
            elif '5':
                break
            else:
                pass

    @classmethod
    def checkout_page(cls, shopping_cart, logger=None):
        """In progress
        """
        if logger is None:
            logger = cls._logger

        print(shopping_cart)
        shopping_cart.build_table()

        while True:

            view = shopping_cart.get_view()
            print(view)

            choice = input(
                "Please choose: "
                "(1) next page, "
                "(2) previous page, "
                "(3) submit order, "
                "(4) cancel order, "
                "Any other key to exit "
            )
            if choice not in ('1', '2', '3', '4'):
                break

            if choice=='1':  # next page
                shopping_cart.next_page()
            elif choice=='2':  # previous page
                shopping_cart.prev_page()
            elif choice=='3':  # add item to cart
                # enter results to database
                pass
            else:
                shopping_cart.reset()


        print(shopping_cart.items)  # shopping cart should probably be implemented as a dataframe

    @classmethod
    def review_page(cls, logger=None):
        if logger is None:
            logger = cls._logger
            
        pass
