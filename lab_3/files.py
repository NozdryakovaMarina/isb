import json

from typing import Dict


def get_bytes(name: str) -> bytes:
    """
    Reading data in bytes from a file

    Args:
            name: path to the file

    Return:
            bytes: byte data reading from the file
    """
    try:
        with open(name, 'rb') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print(f"The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}.")


def write_bytes(name: str, text: bytes) -> None:
    """
    Writing data in bytes to a file

    Args:
            name: path to the file
            text: data to write in bytes
    """
    try:
        with open(name, mode="wb") as file:
            file.write(text)
        print(f"Congratulations! The data is written to a file : {name}.")
    except FileNotFoundError:
         print(f"The file was not found.")
    except Exception as e:
         print(f"An error occurred while writing the file: {str(e)}.")


def get_txt(name: str) -> str:
    """
     The function is for reading .txt file

    Args:
            name: path to the .txt file

    Returns:
            text from file
    """
    try:
        with open(name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}.")


def write_txt(name: str, text: str) -> None:
    """
     The function for writing text to a file

    Args:
            name: path to the file to write
            text: text to write to a file
    """
    try:
        with open(name, "w", encoding='utf-8') as file:
            file.write(text)
        print(f"Awesome! The data is written to a file : {name}.")
    except FileNotFoundError:
         print(f"The file was not found.")
    except Exception as e:
         print(f"An error occurred while writing the file: {str(e)}.")


def get_json(name: str) -> Dict[str, str]:
    """
     The function is for reading .json file

    Args:
            name: path .json file
    """
    try:
        with open(name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading json the file: {str(e)}.")


def write_json(name: str, data: dict) -> Dict[str, str]:
    """
     The function for writing to a json file

    Args:
            name: path to the file to write
            data: data to write to a file
    """
    try:
        with open(name, 'w', encoding='utf-8') as file:
            return json.dump(data, file, ensure_ascii=False, indent=1)
    except FileNotFoundError:
        print(f"The file was not found.")
    except Exception as e:
        print(f"An error occurred while writing json the file: {str(e)}.")
