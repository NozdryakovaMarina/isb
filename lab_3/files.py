import json

from typing import Dict


def get_bytes(name: str) -> bytes:
    try:
        with open(name, 'rb') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}.")


def write_bytes(name: str, text: bytes) -> None:
    try:
        with open(name, mode="wb") as file:
            file.write(text)
        print(f"Congratulations! The data is written to a file : {name}.")
    except FileNotFoundError:
         print("The file was not found.")
    except Exception as e:
         print(f"An error occurred while write the file: {str(e)}.")


def get_txt(name: str) -> str:
    try:
        with open(name, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}.")


def write_txt(name: str, text: str) -> None:
    try:
        with open(name, "w", encoding='utf-8') as file:
            file.write(text)
        print(f"Awesome! The data is written to a file : {name}.")
    except FileNotFoundError:
         print("The file was not found.")
    except Exception as e:
         print(f"An error occurred while write the file: {str(e)}.")


def get_json(name: str) -> Dict[str, str]:
    try:
        with open(name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred while reading json the file: {str(e)}.")


def write_json(name: str, data: dict) -> Dict[str, str]:
    try:
        with open(name, 'w', encoding='utf-8') as file:
            return json.dump(data, file, ensure_ascii=False, indent=1)
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred while write json the file: {str(e)}.")
