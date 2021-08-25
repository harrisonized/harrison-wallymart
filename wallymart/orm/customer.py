#!/usr/bin/env python3

class Customer:
    """This is used to hold customer profile information. It intentionally
    excludes information about the customer's username, and password.
    For those, see the :class:`Credentials` class.
    """
    def __init__(self,
                 customer_id='',
                 first_name='',
                 last_name='',
                 street_address='',
                 zip_code='',
                ):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name
        self._street_address = street_address
        self._zip_code = zip_code

    # ----------------------------------------------------------------------
    # Getters

    def get_customer_id(self):
        """Get the customer_id. This is redundant to credentials.user_id
        """
        return self._customer_id

    def get_first_name(self):
        """Get the first name
        """
        return self._first_name
    
    def get_last_name(self):
        """Get the last name
        """
        return self._last_name

    def get_street_address(self):
        """Get the street address.
        """
        return self._street_address

    def get_zip_code(self):
        """Get the zip code
        """
        return self._zip_code

    # ----------------------------------------------------------------------
    # Setters

    def set_customer_id(self, customer_id):
        """Set the customer_id. This should only be controlled by the program
        by passing in the value from credentials.user_id.
        """
        self._customer_id = customer_id

    def set_first_name(self, first_name):
        """Set the first_name
        """
        self._first_name = first_name
    
    def set_last_name(self, last_name):
        """Set the last_name
        """
        self._last_name = last_name

    def set_street_address(self, street_address):
        """Set the street address. This should exclude city and state info.
        """
        self._street_address = street_address

    def set_zip_code(self, zip_code):
        """Set the zip_code.
        """
        self._zip_code = zip_code
