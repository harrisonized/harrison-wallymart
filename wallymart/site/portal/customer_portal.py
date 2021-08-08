#!/usr/bin/env python3

"""Customer pages
"""

class CustomerPortal:
    """Inherit through Pages
    """

    # ----------------------------------------------------------------------
    # Public

    def customer_home(self, logger=None, username='default_customer'):
        # automatically display items
        # write review
        print(f'Wecome {username}')