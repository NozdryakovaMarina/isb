import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

from files import *


class Symmetric:

    def __init__(self):
        self.key = None

    def generation_symmetric_key(self) -> bytes:
        self.key = os.urandom(16)
        return self.key

    def serialization_symmetric_key(self, file_name: str) -> None:
        write_bytes(file_name, self.key)

    @staticmethod
    def deserialization_symmetric_key(file_name: str) -> bytes:
        key = get_bytes(file_name)
        return key

    def encrypted_text(self, file_name: str, encryption_path: str, key: bytes) -> bytes:

        padder = padding.PKCS7(128).padder()
        text = get_bytes(file_name)
        padded_text = padder.update(text) + padder.finalize()

        iv = os.urandom(16)
        symmetric_key = self.deserialization_symmetric_key(key)
        cipher = Cipher(algorithms.SEED(symmetric_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        c_text = encryptor.update(padded_text) + encryptor.finalize()
        c_text = iv + c_text
        write_bytes(encryption_path, c_text)

        return c_text

    def decrypted_text(self, encryption_path: str, key: bytes, decryptor_path: str) -> str:

        en_text = get_bytes(encryption_path)

        iv = en_text[:16]
        key = self.deserialization_symmetric_key(key)
        cipher = Cipher(algorithms.SEED(key), modes.CBC(iv))

        en_text = en_text[16:]

        decryptor = cipher.decryptor()
        dc_text = decryptor.update(en_text) + decryptor.finalize()

        unpadder = padding.PKCS7(128).unpadder()
        unpadder_dc_text = unpadder.update(dc_text) +  unpadder.finalize()

        write_txt(decryptor_path, unpadder_dc_text.decode('UTF-8'))

        return unpadder_dc_text.decode('UTF-8')
 