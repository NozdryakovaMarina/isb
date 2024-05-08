import os

class Symmetric:

    def __init__(self, key):
        self.key = None

    def generetion_symmetric_key(self) -> bytes:
        return os.urandom(16)