#!/usr/bin/env python3

from .credential_encoder import CredentialEncoder

class Credentials:
    def __init__(self, username='', password=''):
        self._user_id = 0  # get from database
        self._username = username
        self._password = password  # only save encrypted
        if self._password != '':
            self._password = CredentialEncoder(self._password, 'sha256').item

    # ----------------------------------------------------------------------
    # Public

    def set_user_id(self, user_id):
        self._user_id = user_id

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = CredentialEncoder(password, 'sha256').item

    def get_user_id(self):
        return self._user_id

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password  
