#!/usr/bin/env python3

class OrderItem:
    def __init__(self, product_id=None, quantity=1):
        self.product_id = product_id  # instance of the product class
        self.quantity = quantity

    def set_product_id(self, product_id):
       self.product_id = product_id

    def set_quantity(self, quantity):
      self.quantity = quantity