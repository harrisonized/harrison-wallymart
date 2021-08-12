#!/usr/bin/env python3

class Product:
    """Container used to hold data from the database
    """
    def __init__(self,
                 product_name='',
                 description='',
                 quantity=0,
                 price=0,
                ):
        self.product_name = product_name
        self.description = description
        self.quantity = quantity
        self.price = price

    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_description(self, description):
        self.description = description

    def set_quantity(self, quantity:int):
        self.quantity = quantity

    def set_price(self, price):
        self.price = price

    def get_product_name(self):
        return self.product_name

    def get_description(self):
        return self.description

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price
