#!/usr/bin/env python3

class Product:
    """Container used to hold product information prior to writing it to the 
    database. This information is entered by the employee and updated using
    the appropriate getters and setters.

    :ivar str product_name: The name of the product. This must be unique, since \
    it is used to identify the product.
    :ivar str description: A short description of the product.
    :ivar int quantity: How much inventory is in stock.
    :ivar float price: This is rounded to the nearest cent.
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

    # ----------------------------------------------------------------------
    # Getters

    def get_product_name(self):
        return self.product_name

    def get_description(self):
        return self.description

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

    # ----------------------------------------------------------------------
    # Setters

    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_description(self, description):
        self.description = description

    def set_quantity(self, quantity:int):
        self.quantity = quantity

    def set_price(self, price):
        self.price = price
