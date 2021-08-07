#!/usr/bin/env python3

import logging
from wallymart.credential_manager.credentials import Credentials

class Pages:

    # ----------------------------------------------------------------------
    # Public

    def home_page(self, logger):
        """Home page
        Need seperate login for employees
        """
        logger.log("""Welcome to Wallymart""")  # put something pretty here
        while True:
            sign_up_or_log_in = input("Please choose: (1) sign up, (2) log in: ")
            if sign_up_or_log_in not in ('1', '2'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(f"Please choose: (1) sign up, (2) log in: {sign_up_or_log_in}")
        return sign_up_or_log_in

    def signup_page(self, logger):
        username = input("Username: ")
        password = input("Password: ")
        self._credentials = Credentials(username, password)
        logger.log(
            f"username: {self._credentials.get_username()} \n" \
            f"password: {self._credentials.get_password()}"
        )

    def login_page(self, logger):
        username = input("Username: ")
        password = input("Password: ")
        self._credentials = Credentials(username, password)
        logger.log(
            f"username: {self._credentials.get_username()} \n" \
            f"password: {self._credentials.get_password()}"
        )
        return True

    def customer_portal(self, logger):
        # automatically display items
        # write review
        pass

    def employee_portal(self, logger):
        # display items that need to be delivered
        # be able to mark items that are delivered
        pass
