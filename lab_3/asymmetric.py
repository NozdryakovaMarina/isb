import os 

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


class Asymmetric:

    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generation_asymmetric_keys(self) -> None:
        keys = rsa.generate_private_key(
            public_exponent = 65537,
            key_size = 2048
        )

        self.private_key = keys
        self.public_key = keys.public_key()