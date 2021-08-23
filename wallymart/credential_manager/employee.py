#!/usr/bin/env python3

import datetime as dt

class Employee:
    """Container used to hold data from the database
    Should be instantiated when authenticated
    """
    def __init__(self,
                 employee_id=0,
                 first_name='',
                 last_name='',
                ):
        self._employee_id = employee_id
        self._first_name = first_name
        self._last_name = last_name

    # ----------------------------------------------------------------------
    # Getters

    def get_employee_id(self):
        return self._employee_id

    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self):
        return self._last_name

    # ----------------------------------------------------------------------
    # Setters

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_first_name(self, first_name):
        self._first_name = first_name
    
    def set_last_name(self, last_name):
        self._last_name = last_name
