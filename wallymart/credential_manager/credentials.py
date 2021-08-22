#!/usr/bin/env python3

from .credential_encoder import CredentialEncoder

class Credentials:
    def __init__(self, username='', password=''):
        self._customer_id = 0  # get from database
        self._username = username
        self._password = password  # only save encrypted
        if self._password != '':
            self._password = CredentialEncoder(self._password, 'sha256').item

    # ----------------------------------------------------------------------
    # Public

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = CredentialEncoder(password, 'sha256').item

    def get_customer_id(self):
        return self._customer_id

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password  
