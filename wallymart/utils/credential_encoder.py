#!/usr/bin/env python3

import hashlib


class CredentialEncoder:
    """Use this before saving credentials to database
    
    Note: one-way hashing will mean the user is unable to retrieve their data if they forget
    Should probably make this a 2-way hashing...
    This might be okay for now
    """
    def __init__(self, item, hash_algorithm='md5', encoding='utf-8'):
        self.item = item
        self.encoding = encoding
        self.hash_algorithm = hash_algorithm
        self.encode()
        
    def encode(self, hash_algorithm=None):
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
