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
            dict: a dictionary in which the key is a symbol and the value is a frequency
    """
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ.,?:— "
    a = ''.join(filter(lambda x: x in alphabet, get_txt(name))) 
    return {i: a.count(i) for i in set(a)}
    # print({i: a.count(i) for i in set(a)})


def main() -> None:
    
    name = 'lab_1/task1/original.txt'
    # get_txt(name)

    # name_json = 'lab_1/task1/key.json'
    # get_json(name_json) 

    get_frequency(name)