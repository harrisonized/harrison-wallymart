#!/usr/bin/env python3

"""Employee pages
"""

import logging


class EmployeePortal:
    """All methods are class methods so do not require instantiating the class
    This class is meant to be inherited by Pages
    """

    # ----------------------------------------------------------------------
    # Public

    @staticmethod
    def home(username, logger):

        logger.log(f'Welcome {username}...')
        while True:
            choice = input(
                "Please choose: "
                "(1) view delivery items, "
                "(2) view products, "  # shared
                "(3) view specific item, "  # shared
                "(4) add products, "
                "(5) update profile, "  # shared
                "(6) log out: "
            )
            if choice not in ('1', '2', '3', '4', '5', '6'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(
            "Please choose: "
            "(1) view delivery items, "
            "(2) view products, "
            "(3) view specific item, "
            "(4) add products, "
            "(5) update profile, "
            "(6) log out: "
            f"{choice}"
        )
        return choice

    # see: https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name
    __home = home  # local reference

    @classmethod
    def employee_home(cls, username):
        """Requires that cls._logger be used as the logger
        """
        return cls.__home(username, cls._logger)

    @classmethod
    def delivery_page(cls, logger=None):
        if logger is None:
            logger = cls._logger

    @classmethod
    def add_products_page(cls, logger=None):
        if logger is None:
            logger = cls._logger
    