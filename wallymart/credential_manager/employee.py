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
                 start_date='',
                 end_date='',
                 is_current=True,
                ):
        self._employee_id = employee_id
        self._first_name = first_name
        self._last_name = last_name
        self._start_date = start_date
        self._end_date = end_date
        self._is_current = is_current

    # ----------------------------------------------------------------------
    # Getters

    def get_id(self):
        return self._employee_id

    def get_first_name(self):
        return self._first_name
    
    def get_last_name(self):
        return self._last_name

    def get_start_date(self):
        return self._start_date

    def get_end_date(self):
        return self._end_date

    def get_is_current(self):
        return self._is_current

    # ----------------------------------------------------------------------
    # Setters

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id

    def set_first_name(self, first_name):
        self._first_name = first_name
    
    def set_last_name(self, last_name):
        self._last_name = last_name

    def set_start_date(self, start_date):
        self._start_date = start_date

    def set_end_date(self, end_date):
        self._end_date = end_date

    def set_is_current(self, is_current):
        self._is_current = is_current
