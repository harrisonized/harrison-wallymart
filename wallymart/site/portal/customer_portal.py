#!/usr/bin/env python3

"""Customer pages
"""

import logging
import json
import pandas as pd

from wallymart.utils.database_connection import DatabaseConnection
from wallymart.orm.customer import Customer


class CustomerPortal:
    """This class is meant to be inherited by Pages
    """

    # ----------------------------------------------------------------------
    # Public

    @staticmethod
    def home(logger):
        """Customer Home Page. Prompts the customer to view products, checkout,
        update profile, or log out.
        """
        while True:
            choice = input(
                "Please choose: "
                "(1) view products, "
                "(2) checkout, "
                "(3) update profile, "
                "(4) log out: "
            )
            if choice not in ('1', '2', '3', '4'):
                logger.log("Please pick a valid choice")
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
        """Prompts the customer to view products, checkout, update profile, or log out. Calls upon the 
        :meth:`wallymart.site.portal.customer_portal.CustomerPortal.home` method
        and prevents name conflicts when inherited by Pages.
        """
        return cls.__home(cls._logger)

    @classmethod
    def checkout_page(cls, shopping_cart, logger=None):
        """Enables the customer to view the order items in the shopping cart,
        then choose whether to submit the order or cancel the cart. If the customer
        submits the order, prompts the customer for credit card information.
        """
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

                logger.log(view)
                logger.log(f'Total price: {total_price}')
            else:
                logger.log("No items in cart, returning to home...")
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
                # not implemented at this time
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
                     'total_price': total_price,
                     'is_received': False
                    }
                ])
                database_connection.append(df)
                shopping_cart.reset()
                logger.log("Order submitted!")
                break

            else:
                shopping_cart.reset()

    @classmethod
    def profile_page(cls, customer_id, logger=None):
        """Enables the customer to update their profile.
        """
        if logger is None:
            logger = cls._logger

        database_connection = DatabaseConnection(f"customers.csv")
        table = database_connection.table
        customer = Customer(customer_id)

        view = table[(table['customer_id']==customer.get_customer_id())]
        logger.log(view)

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
                logger.log("Please pick a valid choice")
            elif choice=='1':
                view = table[(table['customer_id']==customer.get_customer_id())]
                logger.log(view)
            elif choice=='2':
                first_name = input("Enter your first name: ")
                customer.set_first_name(first_name)
            elif choice=='3':
                last_name = input("Enter your last name: ")
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
                logger.log("Information saved!")
            else:
                break

    __profile_page = profile_page  # local reference

    @classmethod
    def customer_profile_page(cls, customer_id):
        """Enables the customer to update their profile. Calls upon the 
        :meth:`wallymart.site.portal.customer_portal.CustomerPortal.profile_page`
        method and prevents name conflicts when inherited by Pages.
        """
        return cls.__profile_page(customer_id, cls._logger)
