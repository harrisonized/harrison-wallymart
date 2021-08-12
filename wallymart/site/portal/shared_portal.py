#!/usr/bin/env python3

"""Customer pages
"""

import logging
from wallymart.order_manager.shopping_cart import ShoppingCart
from wallymart.order_manager.product import Product
from wallymart.database_manager.database_connection import DatabaseConnection


class SharedPortal:
    """All methods are class methods so do not require instantiating the class
    This class is meant to be inherited by Pages
    """

    # ----------------------------------------------------------------------
    # Public

    @classmethod
    def view_specific_item(cls, logger=None):
        """Should probably be handled through DatabaseConnection
        """
        if logger is None:
            logger = cls._logger

    @classmethod
    def update_profile_page(cls, username, logger=None):
        if logger is None:
            logger = cls._logger
