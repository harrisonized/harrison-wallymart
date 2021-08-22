#!/usr/bin/env python3

"""Customer pages
"""

import logging
import json
import pandas as pd

from wallymart.database_manager.database_connection import DatabaseConnection
from wallymart.credential_manager.customer import Customer
from wallymart.order_manager.order_item import OrderItem
from wallymart.order_manager.review import Review


class CustomerPortal:
    """All methods are class methods so do not require instantiating the class
    This class is meant to be inherited by Pages
    """

    # ----------------------------------------------------------------------
    # Public

    @staticmethod
    def home(logger):

        while True:
            choice = input(
                "Please choose: "
                "(1) view products, "
                "(2) checkout, "
                "(3) update profile, "
                "(4) log out: "
            )
            if choice not in ('1', '2', '3', '4'):
                print("Please pick a valid choice")
            else:
                break
        logger.log(
            "Please choose: "
            "(1) view products, "
            "(2) checkout, "
            "(3) update profile, "
            "(4) log out: "
            f"{choice}"
        )
        return choice

    # see: https://stackoverflow.com/questions/1301346/what-is-the-meaning-of-single-and-double-underscore-before-an-object-name
    __home = home  # local reference

    @classmethod
    def customer_home(cls):
        """Requires that cls._logger be used as the logger
        """
        return cls.__home(cls._logger)

    @classmethod
    def view_products(cls, shopping_cart, logger=None):
        """Should probably be handled through DatabaseConnection
        """
        if logger is None:
            logger = cls._logger
        database_connection = DatabaseConnection(f"products.csv")

        while True:

            view = database_connection.get_view()
            print(view)

            choice = input(
                "Please choose: "
                "(1) next page, "
                "(2) previous page, "
                "(3) add item to cart, "
                "(4) write a review, "
                "Enter empty to go back "
            )
            if choice not in ('1', '2', '3', '4'):
                break

            if choice=='1':  # next page
                database_connection.next_page()
            elif choice=='2':  # previous page
                database_connection.prev_page()

             # add item to cart
            elif choice=='3':

                order_item = OrderItem()

                # enter product_id
                while True:
                    product_id = input("Enter the product id: ")
                    try:
                        product_id = int(product_id)
                    except:
                        logger.log("product id should be an integer")
                    order_item.set_product_id(product_id)
                    break

                # enter quantity
                while True:
                    quantity = input("Enter quantity: ")
                    try:
                        quantity = int(quantity)
                    except:
                        logger.log("quantity should be an integer")
                    order_item.set_quantity(quantity)
                    break

                shopping_cart.append(order_item)

            elif choice=='4':

                review = Review()

                # get product_id
                while True:
                    product_id = input("Enter the product id: ")
                    try:
                        product_id = int(product_id)
                    except:
                        logger.log("product id should be an integer")
                    review.set_product_id(product_id)
                    break

                # enter review
                while True:
                    review_text = input("Enter your review: ")
                    review.set_review_text(review_text)
                    break

                while True:
                    confirm = input("Type 'yes' to confirm your review, "
                                    "Enter empty to exit without saving: ")
                    if confirm == 'yes':

                        # save order to orders table
                        database_connection = DatabaseConnection(f"reviews.csv")
                        last_id = database_connection.table['review_id'].max()
                        if pd.isna(last_id):
                            last_id = 0
                        df = pd.DataFrame.from_records([
                            {'review_id': last_id + 1,
                             'customer_id': shopping_cart.get_customer_id(),
                             'product_id': review.get_product_id(),
                             'review_text': review.get_review_text()
                            }
                        ])
                        database_connection.append(df)
                        break

                    else:
                        break

            else:
                break

    @classmethod
    def checkout_page(cls, shopping_cart, logger=None):

        if logger is None:
            logger = cls._logger

        while True:

            database_connection = DatabaseConnection(f"products.csv")
            
            # view shopping cart
            shopping_cart.build_table()
            if not shopping_cart.table.empty:
                view = shopping_cart.table.set_index('product_id').join(
                    (database_connection.table
                        .set_index('product_id')
                        .drop(columns=['quantity'])
                    ), how='left'
                )
                view['total'] = view['quantity']*view['price']
                total_price = sum(view['total'])

                print(view)
                print(f'Total price: {total_price}')
            else:
                print("No items in cart, returning to home...")
                break

            choice = input(
                "Please choose: "
                "(1) submit order, "
                "(2) cancel order, "
                "Any other key to return to home "
            )
            if choice not in ('1', '2'):
                break

            if choice=='1':

                # placeholder for real credit card auth
                cc_no = input(
                    "Please enter your credit card number. "
                    "Note that we do not save this information."
                )
                expiration_date = input(
                    "Please enter the expiration date."
                )

                # save order to orders table
                database_connection = DatabaseConnection(f"orders.csv")
                last_id = database_connection.table['order_id'].max()
                if pd.isna(last_id):
                    last_id = 0
                df = pd.DataFrame.from_records([
                    {'order_id': last_id + 1,
                     'customer_id': shopping_cart.get_customer_id(),
                     'order': json.dumps(view[
                         ['product_name', 'quantity']
                     ].to_dict('records')), 
                     'total_price': None,
                     'is_received': False
                    }
                ])
                database_connection.append(df)
                shopping_cart.reset()
                print("Order submitted!")
                break

            else:
                shopping_cart.reset()

    @classmethod
    def profile_page(cls, customer_id, logger=None):
        if logger is None:
            logger = cls._logger

        
        table = database_connection.table
        customer = Customer(customer_id)

        view = table[(table['customer_id']==customer.get_customer_id())]
        print(view)

        while True:

            choice = input(
                "Please choose: "
                "(1) check data, "
                "(2) update first name, "
                "(3) update last name, "
                "(4) update street address, "
                "(5) update zip code, "
                "(6) save changes, "
                "(7) exit without saving "
            )
            if choice not in ('1', '2', '3', '4', '5', '6', '7'):
                print("Please pick a valid choice")
            elif choice=='1':
                view = table[(table['customer_id']==customer.get_customer_id())]
                print(view)
            elif choice=='2':
                first_name = input("Enter your first name: ")
                customer.set_first_name(first_name)
            elif choice=='3':
                last_name = input("Enter your first name: ")
                customer.set_last_name(last_name)
            elif choice=='4':
                street_address = input("Enter your street address: ")
                customer.set_street_address(street_address)
            elif choice=='5':
                zip_code = input("Update zip code: ")
                customer.set_zip_code(zip_code)
            elif choice=='6':
                table[
                    (table['customer_id']==customer.get_customer_id())
                ] = pd.Series(
                    {'customer_id': customer.get_customer_id(),
                     'first_name': customer.get_first_name(),
                     'last_name': customer.get_last_name(),
                     'street_address': customer.get_street_address(),
                     'zip_code': customer.get_zip_code()
                    }
                )
                database_connection.overwrite()
                print("Information saved!")
            else:
                break

    __profile_page = profile_page  # local reference

    @classmethod
    def customer_profile_page(cls, customer_id):
        """Requires that cls._logger be used as the logger
        """
        return cls.__profile_page(customer_id, cls._logger)
