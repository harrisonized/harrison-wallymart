#!/usr/bin/env python3

from .credential_encoder import CredentialEncoder

class Credentials:
    def __init__(self, username='', password=''):
        self._username = username
        self._password = password
        if self._username != '':
            self._username = CredentialEncoder(self._username, 'md5').item
        if self._password != '':
            self._password = CredentialEncoder(self._password, 'sha256').item

    # ----------------------------------------------------------------------
    # Public

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password