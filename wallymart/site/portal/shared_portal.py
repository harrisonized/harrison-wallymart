#!/usr/bin/env python3

"""Customer pages
"""

import logging


class SharedPortal:
    def __init__(self, logger=None):
        self._logger = logger or logging.getLogger(__name__)

    # ----------------------------------------------------------------------
    # Public

    def view_products(self, logger=None):
        """Should probably be handled through DatabaseConnection
        """
        if logger is None:
            logger = self._logger

    def view_specific_item(self, logger=None):
        """Should probably be handled through DatabaseConnection
        """
        if logger is None:
            logger = self._logger

    def update_profile_page(self, username, logger=None):
        if logger is None:
            logger = self._logger
