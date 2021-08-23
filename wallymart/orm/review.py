#!/usr/bin/env python3

class Review:
    def __init__(self, product_id=None):
        self._product_id = product_id
        self._review_text = ''

    # ----------------------------------------------------------------------
    # Getters and Setters

    def get_product_id(self):
    	return self._product_id

    def get_review_text(self):
    	return self._review_text

    def set_product_id(self, product_id):
    	self._product_id = product_id

    def set_review_text(self, review_text):
    	self._review_text = review_text
