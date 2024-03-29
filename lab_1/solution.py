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
    cnt = len(get_txt(name))
    a = ''.join(filter(lambda x: x in get_txt(name), get_txt(name))) 
    return {i: a.count(i)/cnt for i in set(a)}


def text_encrypted(filename: str, jsonfile: Dict[str, str]) -> str:
    """
    The function encrypts the text using an encryption key


    Args:
            filename: text for encryption
            jsonfile: encryption key

    Results:
            result: encrypted text
    """
    text = get_txt(filename)
    json_data = get_json(jsonfile)
    sort = dict(sorted(''.join([json_data.get(l, l) for l in text]), reverse=True))
    return sort
    # def decryption(path_encryption: str, path_key: str, path_decryption: str) -> None:
    # key = read_json(path_key)
    # decrypted_text = ''
    # text = read_file(path_encryption)
    # for char in text:
    #     if char in key:
    #         decrypted_text += key[char]
    #     else:
    #         decrypted_text += char
    # write_file(path_decryption, decrypted_text)


def decryption_text(filename: str, key: Dict[str, str], new_file: str) -> str:
    """
    """
    k = get_json(key)
    text = get_txt(filename)
    res = ''
    for c in text:
        if c in k:
            res += str(k[c])
        else:
            res += c
    return res


def write_json(name: str, data: dict) -> Dict[str, str]:
    """
    """
    try: 
        with open(name, 'w', encoding='utf-8') as f:
            res = json.dump(data, f, ensure_ascii=False, indent=1)
        return res
    except Exception as e:
        print(f"An error occurred while writing the JSON file: {str(e)}.")


def main() -> None:
    
    name = 'lab_1/task1/original.txt'
    # get_txt(name)

    name_json = 'lab_1/task1/key.json'
    # get_json(name_json) 

    name3 = 'lab_1/task2/decrypted.txt'
    k1 = get_frequency(name3)
    path = 'lab_1/task2/freq.json'
    # write_json(path, 1)
    # text = text_encrypted(name, name_json)

    # name2 = 'lab_1/task1/encrypted.txt'

    # write_txt(name2, text)

    path2 = 'lab_1/task2/cod5.txt'

    t = decryption_text(name3, path, path2)
    write_txt(path2, t)