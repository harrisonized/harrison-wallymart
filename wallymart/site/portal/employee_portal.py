#!/usr/bin/env python3

"""Employee pages
"""

class EmployeePortal:
    """Inherit through Pages
    """

    # ----------------------------------------------------------------------
    # Public

    def employee_home(self, logger=None, username='default_employee'):
        # display items that need to be delivered
        # be able to mark items that are delivered
        print(f'Welcome {username}')
