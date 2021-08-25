#!/usr/bin/env python3

from wallymart.utils.credential_encoder import CredentialEncoder

class Credentials:
    """This is instantiated during the signup or login process and passed
    to the main program. It holds the user_id and username of the user
    during the lifecycle of the program.
    """

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
        """Set the username
        """
        self._username = username

    def set_password(self, password):
        """Set the password. Note that passwords are immediately hashed using
        :class:`wallymart.utils.credential_encoder.CredentialEncoder`
        """
        self._password = CredentialEncoder(password, 'sha256').item

    def get_user_id(self):
        """Get the user_id. This is an index used to match customer information
        across tables.
        """
        return self._user_id

    def get_username(self):
        """Get the username. This is used to display the username in the customer or
        employee home pages.
        """
        return self._username

    def get_password(self):
        return self._password  
