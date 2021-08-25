#!/usr/bin/env python3

import datetime as dt

class Employee:
    """This is used to hold employee profile information. It intentionally
    excludes information about the employee's username, and password.
    For those, see the :class:`Credentials` class.
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
        """Get the employee_id. This is redundant to credentials.user_id
        """
        return self._employee_id

    def get_first_name(self):
        """Get the first name
        """
        return self._first_name
    
    def get_last_name(self):
        """Get the last name
        """
        return self._last_name

    # ----------------------------------------------------------------------
    # Setters

    def set_employee_id(self, employee_id):
        """Set the employee_id. This should only be controlled by the program
        by passing in the value from credentials.user_id.
        """
        self._employee_id = employee_id

    def set_first_name(self, first_name):
        """Set the first_name
        """
        self._first_name = first_name
    
    def set_last_name(self, last_name):
        """Set the last_name
        """
        self._last_name = last_name
