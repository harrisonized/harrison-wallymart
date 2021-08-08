#!/usr/bin/env python3

"""Customer pages
"""

class CustomerPortal:
    def __init__(self, logger=None):
        self._logger = logger or logging.getLogger(__name__)

    # ----------------------------------------------------------------------
    # Public

    def customer_home(self, logger=None, username='default_customer'):
        # automatically display items
        # write review
        print(f'Wecome {username}')