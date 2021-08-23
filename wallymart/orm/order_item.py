#!/usr/bin/env python3

class OrderItem:
    def __init__(self, product_id=None, quantity=1):
        self._product_id = product_id  # instance of the product class
        self._quantity = quantity

    # ----------------------------------------------------------------------
    # Getters and Setters

    def get_product_id(self):
    	return self._product_id

    def get_quantity(self):
    	return self._quantity

    def set_product_id(self, product_id):
    	self._product_id = product_id

    def set_quantity(self, quantity):
    	self._quantity = quantity
