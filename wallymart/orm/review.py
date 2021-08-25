#!/usr/bin/env python3

class Review:
    """Container used to hold review information prior to writing it to the
    database. This information is entered by the customer. Since we can use
    the database to get the rest of the product information, the 
    :class:`Review` class only stores the product_id rather than the full
    product information.
    """
    def __init__(self, product_id=None):
        self._product_id = product_id
        self._review_text = ''

    # ----------------------------------------------------------------------
    # Getters and Setters

    def get_product_id(self):
        """Get the product_id
        """
        return self._product_id

    def get_review_text(self):
        """Get the user-entered review_text
        """
        return self._review_text

    def set_product_id(self, product_id):
        """Set the product_id
        """
        self._product_id = product_id

    def set_review_text(self, review_text):
        """Set the user-entered review_text
        """
        self._review_text = review_text
