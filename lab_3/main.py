import argparse

from enum import Enum

from symmetric import Symmetric
from asymmetric import Asymmetric
from files import FilesHelper


class Direction(Enum):
    SYMMETRIC_KEY = 0
    ASYMMETRIC_KEY = 1
    TEXT_ENCRYPTION = 2
    TEXT_DECRYPTION = 3
    SYMMETRIC_KEY_ENCRYPTION = 4
    SYMMETRIC_KEY_DECRYPTION = 5


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Hybrid cryptosystem")
    parser.add_argument('-dir', '--direction', type=int,
                        help='Mode selection:'
                        '0 — symmetric key generation'
                        '1 — asymmetric key generation'
                        '2 — text encryption'
                        '3 — text decryption'
                        '4 — symmetric key encryption'
                        '5 — symmetric key decryption')
    parser.add_argument('-s', '--settings', type=str,
                        help='Path to the user settings file')

    args = parser.parse_args()

    symmetric = Symmetric()
    asymmetric = Asymmetric()
    settings = FilesHelper.get_json(args.settings)

    match(int(args.direction)):
        case Direction.SYMMETRIC_KEY.value:
            symmetric_key = symmetric.generation_symmetric_key()
            symmetric.serialization_symmetric_key(settings['symmetric_key'])
        case Direction.ASYMMETRIC_KEY.value:
            asymmetric_key = asymmetric.generation_asymmetric_keys()
            asymmetric.serialization_private_key(settings['private_key'])
            asymmetric.serialization_public_key(settings['public_key'])
        case Direction.TEXT_ENCRYPTION.value:
            symmetric.encrypted_text(settings['original_text'],
            settings['encrypted_text'], settings['symmetric_key'])
        case Direction.TEXT_DECRYPTION.value:
            symmetric.decrypted_text(settings['encrypted_text'],
            settings['symmetric_key'], settings['decrypted_text'])
        case Direction.SYMMETRIC_KEY_ENCRYPTION.value:
            asymmetric.encrypt_symmetric_key(settings['public_key'],
            settings['symmetric_key'], settings['encrypt_symmetric_key'])
        case Direction.SYMMETRIC_KEY_DECRYPTION.value:
            asymmetric.decrypt_symmetric_key(settings['private_key'],
            settings['encrypt_symmetric_key'], settings['decrypt_symmetric_key'])
        case _:
            print(f"I can't execute this command(")
             