#!/usr/bin/env python3

import os
import re
import logging
import pandas as pd

class DatabaseConfigurator:
    """Define the database schema
    Instantiates tables if they don't exist
    """
    # config
    filename_for_table_name = {
        'customer_credentials': 'customer_credentials.csv',  # customer_id, customer_username, customer_password
        'customers': 'customers.csv',  # customer_id, first_name, last_name, street_address, zip_code, join_date
        'employee_credentials': 'employee_credentials.csv',  # customer_id, customer_username, customer_password
        'employees': 'employees.csv',  # employee_id, first_name, last_name, start_date, end_date, is_current
        'orders': 'orders.csv',  # order_id, customer_id, order_id, quantity, price, total_price, is_received
        'products': 'products.csv',  # product_id, product_name, description, stock_quantity, price
        'reviews': 'reviews.csv',  # review_id, customer_id, product_id, is_ordered, review_text
    }

    def __init__(self, data_dir='data'):
        self._repo_dir = re.match('^(.*?)harrison-wallymart', os.getcwd()).group()
        self.data_dir = data_dir

    # ----------------------------------------------------------------------
    # Private

    def _create_customer_credentials_table(self):
        filename = self.filename_for_table_name.get('customer_credentials')
        file = f'{self._repo_dir}/{self.data_dir}/{filename}'
        if not os.path.exists(file):
            df = pd.DataFrame(columns=[
                'customer_id',
                'customer_username',
                'customer_password',
            ])
            df.to_csv(f'{self._repo_dir}/{self.data_dir}/{filename}', index=None)
            
    def _create_customers_table(self):
        filename = self.filename_for_table_name.get('customers')
        file = f'{self._repo_dir}/{self.data_dir}/{filename}'
        if not os.path.exists(file):
            df = pd.DataFrame(columns=[
                'customer_id',
                'first_name', 
                'last_name',
                'street_address',
                'zip_code',
                'join_date'
            ])
            df.to_csv(f'{self._repo_dir}/{self.data_dir}/{filename}', index=None)

    def _create_employee_credentials_table(self):
        filename = self.filename_for_table_name.get('employee_credentials')
        file = f'{self._repo_dir}/{self.data_dir}/{filename}'
        if not os.path.exists(file):
            df = pd.DataFrame(columns=[
                'employee_id',
                'employee_username',
                'employee_password',
            ])
            df.to_csv(f'{self._repo_dir}/{self.data_dir}/{filename}', index=None)

    def _create_employees_table(self):
        filename = self.filename_for_table_name.get('employees')
        file = f'{self._repo_dir}/{self.data_dir}/{filename}'
        if not os.path.exists(file):
            df = pd.DataFrame(columns=[
                'employee_id',
                'first_name',
                'last_name',
                'start_date',
                'end_date',
                'is_current',
            ])
            df.to_csv(f'{self._repo_dir}/{self.data_dir}/{filename}', index=None)
        
    def _create_orders_table(self):
        filename = self.filename_for_table_name.get('orders')
        file = f'{self._repo_dir}/{self.data_dir}/{filename}'
        if not os.path.exists(file):
            df = pd.DataFrame(columns=[
                'order_id',
                'customer_id',
                'order_id',
                'quantity',
                'price',
                'total_price',
                'is_received',
            ])
            df.to_csv(f'{self._repo_dir}/{self.data_dir}/{filename}', index=None)
            
    def _create_products_table(self):
        filename = self.filename_for_table_name.get('products')
        file = f'{self._repo_dir}/{self.data_dir}/{filename}'
        if not os.path.exists(file):
            df = pd.DataFrame(columns=[
                'product_id',
                'product_name',
                'description',
                'stock_quantity',
                'price',
            ])
            df.to_csv(f'{self._repo_dir}/{self.data_dir}/{filename}', index=None)
            
    def _create_reviews_table(self):
        filename = self.filename_for_table_name.get('reviews')
        file = f'{self._repo_dir}/{self.data_dir}/{filename}'
        if not os.path.exists(file):
            df = pd.DataFrame(columns=[
                'review_id',
                'customer_id',
                'product_id',
                'is_ordered',
                'review_text',
            ])
            df.to_csv(f'{self._repo_dir}/{self.data_dir}/{filename}', index=None)

    # ----------------------------------------------------------------------
    # Public

    def initialize_database(self):
        os.makedirs('data', exist_ok=True)
        self._create_customer_credentials_table()
        self._create_customers_table()
        self._create_employee_credentials_table()
        self._create_employees_table()
        self._create_orders_table()
        self._create_products_table()
        self._create_reviews_table()
