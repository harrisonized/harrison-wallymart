#!/usr/bin/env python3

class OrderItem:
    def __init__(self, product_id=None, quantity=1):
        """Container used to hold order information prior to writing it to the
        database. This information is entered by the customer. Since we can use
        the database to get the rest of the product information, the 
        :class:`OrderItem` class only stores the product_id rather than the full
        product information.
        """
        self._product_id = product_id
        self._quantity = quantity

    # ----------------------------------------------------------------------
    # Getters and Setters

    def get_product_id(self):
        """Get the product_id
        """
        return self._product_id

    def get_quantity(self):
        """Get the user-entered quantity
        """
        return self._quantity

    def set_product_id(self, product_id):
        """Set the product_id
        """
        self._product_id = product_id

    def set_quantity(self, quantity):
        """Set the user-entered quantity
        """
        self._quantity = quantity
