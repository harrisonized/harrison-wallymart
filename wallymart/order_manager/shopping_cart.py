#!/usr/bin/env python3


class ShoppingCart:
    """Stack holding Items
    """
    def __init__(self):
        self.customer_id = ''
        self.items = []

    def set_customer_id(self, customer_id):
        """Add instances of the Product class
        """
        self.customer_id = customer_id

    def append(self, item):
        """Add instances of the Product class
        """
        self.items.append(item)
