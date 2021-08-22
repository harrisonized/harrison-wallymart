#!/usr/bin/env python3


class Customer:
    """Container used to hold data from the database
    Should be instantiated when authenticated
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
        return self._customer_id

    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self):
        return self._last_name

    def get_street_address(self):
        return self._street_address

    def get_zip_code(self):
        return self._zip_code

    # ----------------------------------------------------------------------
    # Setters

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_first_name(self, first_name):
        self._first_name = first_name
    
    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_street_address(self, street_address):
        self._street_address = street_address

    def set_zip_code(self, zip_code):
        self._zip_code = zip_code
