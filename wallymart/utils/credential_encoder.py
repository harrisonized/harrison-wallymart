#!/usr/bin/env python3

import hashlib


class CredentialEncoder:
    """This is called by the :class:`Credentials` class to hash an item
    prior to storing it. This is great for security. However, one-way hashing
    means the user will be unable to retrieve their passsword if they forget.
    In this scenario, the user should make a new account. Otherwise, a database
    administrator can help with account deletion.

    :parameter str item: Stores the item to be hashed. The item is hashed at \
    initialization.
    :parameter str hash_algorithm: Choose between "md5" and "sha256"
    :parameter str encoding: Default is 'utf-8', but you can change this to arrive \
    at a different hash.
    """
    def __init__(self, item, hash_algorithm='md5', encoding='utf-8'):
        self.item = item
        self.encoding = encoding
        self.hash_algorithm = hash_algorithm
        self.encode()
        
    def encode(self, hash_algorithm=None):
        """
        """
        if hash_algorithm is None:
            hash_algorithm = self.hash_algorithm
        switch = {
            'md5': lambda x: self.encode_md5(x),  # username
            'sha256': lambda x: self.encode_sha256(x),  # password
        }
        self.item = switch[hash_algorithm](self.item)
        
    def encode_md5(self, item):
        return hashlib.md5(self.item.encode(self.encoding)).hexdigest()

    def encode_sha256(self, item):
        return hashlib.sha256(self.item.encode(self.encoding)).hexdigest()
