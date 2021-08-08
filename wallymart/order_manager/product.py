#!/usr/bin/env python3

class Product:
	"""Container used to hold data from the database
	"""
    def __init__(self, product_id, product_name, price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
