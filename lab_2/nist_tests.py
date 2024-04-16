import json
import math

from typing import Dict

from const import path


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
        print(f"An error occurred while reading json the file: {str(e)}.")


def frequency_bitwise_test(name: str) -> float:
    """
    The function checks whether the sequence is random enough

    Args:
            name: path .json file
    
    Returns: 
            P-value is the probability that the generator produces values comparable to the reference
    """
    s = abs(sum([1 if i == "1" else -1 for i in name]))/math.sqrt(len(name))
    print(math.erfc(s/math.sqrt(2)))


def main() -> None:
    name = get_json(path)["cpp"]
    frequency_bitwise_test(name)


if __name__ == "__main__":
    main()
