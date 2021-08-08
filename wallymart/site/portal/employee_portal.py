#!/usr/bin/env python3

"""Employee pages
"""

import logging

class EmployeePortal:
    def __init__(self, logger=None):
        self._logger = logger or logging.getLogger(__name__)

    # ----------------------------------------------------------------------
    # Public

    def employee_home(self, username, logger=None):
        if logger is None:
            logger = self._logger

        logger.log(f'Welcome {username}...')
        while True:
            employee_choice = input(
                "Please choose: "
                "(1) view delivery items, "
                "(2) view products, "
                "(3) add products, "
                "(4) update profile, "
                "(5) log out: "
            )
            if employee_choice not in ('1', '2', '3', '4', '5'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(
            "Please choose: "
            "(1) view delivery items, "
            "(2) view products, "
            "(3) add products, "
            "(4) update profile, "
            f"(5) log out: {employee_choice}"
        )
        return employee_choice

    def delivery_page(self, logger=None):
        if logger is None:
            logger = self._logger

    def view_products_page(self, logger=None):
        if logger is None:
            logger = self._logger

    def add_products_page(self, logger=None):
        if logger is None:
            logger = self._logger
        
    def update_profile_page(self, username, logger=None):
        if logger is None:
            logger = self._logger
