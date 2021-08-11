#!/usr/bin/env python3

"""Customer pages
"""

import logging

class CustomerPortal:
    """All methods are class methods so do not require instantiating the class
    This class is meant to be inherited by Pages
    """

    # ----------------------------------------------------------------------
    # Public

    @classmethod
    def customer_home(cls, username, logger=None):
        if logger is None:
            logger = cls._logger
        logger.log(f'Wecome {username}')
        while True:
            choice = input(
                "Please choose: "
                "(1) view products, "  # shared
                "(2) view specific item, "  # shared
                "(3) add item to cart, "
                "(4) review an item, "
                "(5) checkout, "  # go to shopping_cart page
                "(6) update profile, "
                "(7) log out: "
            )
            if choice not in ('1', '2', '3', '4', '5', '6', '7'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(
            "Please choose: "
            "(1) view products, "
            "(2) view specific item, "
            "(3) add item to cart, "
            "(4) review an item, "
            "(5) checkout, "
            "(6) update profile, "
            "(7) log out: "
            f"{choice}"
        )
        return choice

    @classmethod
    def shopping_cart_page(cls, logger=None):
        if logger is None:
            logger = cls._logger

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
