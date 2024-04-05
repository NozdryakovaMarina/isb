import os
import json

from typing import Dict


def get_txt(name: str) -> str:
    """
    The function is for reading .txt file

    Args:
            name: path to the .txt file

    Returns:
            data: text from file
    """
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}.")


def get_json(name: str) -> Dict[str, str]:
    """
    The function is for reading .json file

    Args:
            name: path .json file

    Returns:
            data: key dictionary
    """
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading JSON the file: {str(e)}.")


def write_txt(name: str, text: str) -> None:
    """
    The function for writing text to a file

    Args:
            name: path to the file to write
            text: text to write to a file
    """
    try:
        with open(name, 'w', encoding='utf-8') as file:
            file.write(text)
        return None
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred while writing the file: {str(e)}.")


def get_frequency(name: str) -> Dict[str, str]:
    """
    The function counts the frequency of characters appearing in the text

    Args:
            name: text for analysis

    Results:
            dict: a dictionary in which the key is
            a symbol and the value is a frequency
    """
    cnt = len(get_txt(name))
    a = ''.join(filter(lambda x: x in get_txt(name), get_txt(name)))
    b = {i: a.count(i)/cnt for i in set(a)}
    sort = dict(sorted(b.items(), key=lambda x: x[1], reverse=True))
    return sort


def text_encrypted(name: str, key: Dict[str, str]) -> str:
    """
    The function encrypts the text using an encryption key

    Args:
            filename: text for encryption
            jsonfile: encryption key

    Results:
            result: encrypted text
    """
    text = get_txt(name)
    json_data = get_json(key)
    s = ''.join([json_data.get(letter, letter) for letter in text])
    return s


def decryption_text(name: str, key: Dict[str, str]) -> str:
    """
    The function decrypts the text using the encryption key

    Args:
            name: encrypted text
            key: json file with an encryption key

    Results:
            text: decrypted text
    """
    text = get_txt(name)
    dict1 = get_json(key)
    text2 = ''
    for letter in text:
        text2 += letter.replace(letter, dict1[letter])
    return text2


def write_json(name: str, data: dict) -> Dict[str, str]:
    """
    The function for writing to a json file

    Args:
            name: path to the file to write
            data: data to write to a file
    """
    try:
        with open(name, 'w', encoding='utf-8') as f:
            res = json.dump(data, f, ensure_ascii=False, indent=1)
        return res
    except Exception as e:
        print(f"An error occurred while writing the JSON file: {str(e)}.")


def main() -> None:
 
    path = get_json("lab_1/path.json")
    encrypted_task2 = path["text_encrypted_task2"]
    key = path["key_task2"]
    decrypted_task2 = path["text_decrypted_task2"]
    t = decryption_text(encrypted_task2, key)
    write_txt(decrypted_task2, t)


if __name__ == "__main__":
    main()
