#!/usr/bin/env python3

import pandas as pd
from wallymart.orm.order_item import OrderItem


class ShoppingCart:
    def __init__(self, items=[]):
        self.customer_id = ''
        self.items = items
        self.table = pd.DataFrame(columns=['product_id', 'quantity'])

    # ----------------------------------------------------------------------
    # Getters and Setters

    def set_customer_id(self, customer_id):
        self.customer_id = customer_id

    def get_customer_id(self):
        return self.customer_id

    def append(self, item):
        """Add instances of the OrderItem class
        """
        if isinstance(item, OrderItem):
            self.items.append(item)
        else:
            raise ValueError("Please enter an OrderItem")

    def reset(self):
        """Remove all items from the shopping cart
        """
        self.items = []
        self.table = pd.DataFrame(columns=['product_id', 'quantity'])

    def build_table(self):
        """Have basics in place, need to make this pretty
        """
        pd.options.display.max_rows = None
        self.table = self.table.append(
            pd.DataFrame(
                {"product_id": [item.get_product_id() for item in self.items],
                 "quantity": [item.get_quantity() for item in self.items]})
        )
