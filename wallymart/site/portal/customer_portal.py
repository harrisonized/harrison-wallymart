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
                "(1) view products, "  # shared
                "(2) checkout, "  # go to shopping_cart page
                "(3) update profile, "
                "(4) log out: "
            )
            if choice not in ('1', '2', '3', '4'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(
            "Please choose: "
            "(1) view products, "
            "(2) checkout, "
            "(3) update profile, "
            "(4) log out: "
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
                "Any key to exit "
            )
            if choice not in ('1', '2', '3', '4'):
                break

            if choice=='1':
                database_connection.next_page()
            elif choice=='2':
                database_connection.prev_page()
            elif choice=='3':
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
            else:
                pass

    @classmethod
    def checkout_page(cls, shopping_cart, logger=None):
        """In progress
        """
        if logger is None:
            logger = cls._logger
        print(shopping_cart.items)

    @classmethod
    def review_item_page(cls, logger=None):
        if logger is None:
            logger = cls._logger

    # ----------------------------------------------------------------------
    # Customer Pages

    # Customer Portal
    # list products automatically (10 per page, loop)
    # Select an option:
    # (0): Log out
    # (1): Update profile
    # (2): View item -> sends to item page
    # (3): Add item to cart
    # (4): Checkout  -> sends to checkout

    # Item page (from view item option)
    # display reviews automatically (10 per page, loop)
    # Select an option: 
    # (0): Log out
    # (1): Add item to cart
    # (2): Select a review -> sends to review page
    # (2): Write a review -> sends to form
    # (3): Go back to customer portal

    # Review page
    # display full review
    # (0): Log out
    # (1): Upvote review
    # (2): Downvote review
    # (3): Go back to item page
    # (4): Go back to customer portal

    # Review form
    # enter a review
    # need logic to only add one review per customer
    # (0): Log out
    # (1): Submit review  # overwrite existing review
    # (2): Go back to item page

    # Checkout page
    # add cart to orders table
    # (1): Add credit card info
    # (2): Add shipping address
    # (3): Submit order -> return to customer portal
