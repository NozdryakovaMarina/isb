import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from typing import Tuple

from symmetric import Symmetric
from files import *


class Asymmetric:
    """
     Class for working with a asymmetric encryption algorithm
    """
    def __init__(self):
        """Constructor"""
        self.private_key = None
        self.public_key = None

    def generation_asymmetric_keys(self) -> Tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """
        Generating a key pair for an asymmetric encryption algorithm

        Return:
                 Tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]: pair of keys
        """
        keys = rsa.generate_private_key(
            public_exponent = 65537,
            key_size = 2048
        )

        self.private_key = keys
        self.public_key = keys.public_key()
        return self.private_key, self.public_key

    def serialization_public_key(self, file_name: str) -> None:
        """
        Serializing the public key to a file

        Args:
                file_name: path to the file to record the public key
        """
        with open(file_name, 'wb') as public_out:
            public_out.write(self.public_key.public_bytes
                            (encoding=serialization.Encoding.PEM,
                            format=serialization.PublicFormat.SubjectPublicKeyInfo))

    def serialization_private_key(self, file_name: str) -> None:
        """
        Serializing the private key to a file

        Args:
                file_name: path to the file to record the private key
        """
        with open(file_name, 'wb') as private_out:
            private_out.write(self.private_key.private_bytes(
                             encoding=serialization.Encoding.PEM,
                             format=serialization.PrivateFormat.TraditionalOpenSSL,
                             encryption_algorithm=serialization.NoEncryption()))

    def deserialization_public_key(self, file_name: str) -> bytes:
        """
        Deserialization of the public key

        Args:
                file_name: path to the public key file
        """
        with open(file_name, 'rb') as pem_in:
            public_bytes = pem_in.read()
        self.public_key = load_pem_public_key(public_bytes)
        return self.public_key

    def deserialization_private_key(self, file_name: str) -> bytes:
        """
        Deserialization of the private key

        Args:
                file_name: path to the private key file
        """
        with open(file_name, 'rb') as pem_in:
            private_bytes = pem_in.read()
        self.private_key = load_pem_private_key(private_bytes, password=None,)
        return self.private_key

    def encrypt_symmetric_key(self, path_public: str, path_symmetric: str,  path_encrypted: str) -> None:
        """
        Text encryption using RSA-OAEP and writing to a file

        Args:
                path_public: path to the public key file
                path_symmetric: path to the symmetric key file
                path_encrypted: path to the encrypted symmetric key file
        """
        public_key = self.deserialization_public_key(path_public)
        symmetric_key = Symmetric.deserialization_symmetric_key(path_symmetric)
        c_text = public_key.encrypt(symmetric_key, padding.OAEP
                            (mgf=padding.MGF1(algorithm=hashes.SHA256()),
                             algorithm=hashes.SHA256(), label=None))

        write_bytes(path_encrypted, c_text)


    def decrypt_symmetric_key(self, path_private: str, path_encrypted: str, path_decrypted: str) -> None:
        """
        Decryption of text by an asymmetric algorithm  and writing to a file
        
        Args:
                path_private: path to the private key file
                path_encrypted: path to the encrypted symmetric key file
                path_decrypted: path to the decrypted symmetric key file
        """
        private_key = self.deserialization_private_key(path_private)
        encrypted_sym_key = Symmetric.deserialization_symmetric_key(path_encrypted)
        dc_text = private_key.decrypt(encrypted_sym_key,
                              padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                              algorithm=hashes.SHA256(), label=None))

        write_bytes(path_decrypted, dc_text)
