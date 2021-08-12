#!/usr/bin/env python3

import pandas as pd
from wallymart.order_manager.order_item import OrderItem


class ShoppingCart:
    """Stack holding Items
    """
    def __init__(self, items=[]):
        self.customer_id = ''
        self.items = items
        self.table = pd.DataFrame(
        	columns=['product_id', 'quantity']
    	)
        self.num_items_per_page = 5
        self.page = 1

    def set_customer_id(self, customer_id):
        """Add instances of the Product class
        """
        self.customer_id = customer_id

    def append(self, item):
        """Add instances of the Product class
        """
        self.items.append(item)

    def reset(self):
        """Remove all items from the shopping cart
        """
        self.items = []

    def get_view(self):
        view = self.table[(self.page-1)*self.num_items_per_page:self.page*self.num_items_per_page]
        return view

    def next_page(self):
        if self.page*self.num_items_per_page <= len(self.table):
            self.page += 1

    def prev_page(self):
        if self.page > 1:
            self.page -= 1
        
    def build_table(self):
        """Have basics in place, need to make this pretty
        """
        pd.options.display.max_rows = None
        self.table = self.table.append(
            pd.DataFrame(
                {"product_id": [item.product_id for item in self.items],
                 "quantity": [item.quantity for item in self.items]})
        )
