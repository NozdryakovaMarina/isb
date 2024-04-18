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
            P-value is the probability that the
            generator produces values comparable to the reference
    """
    s = abs(sum(1 if i == "1" else -1 for i in name))/math.sqrt(len(name))
    return math.erfc(s/math.sqrt(2))


def identical_consecutive_bits_test(name: str):
    """
    The function searches for all sequences of identical bits,
    and then analyzes how much the number and sizes of these
    sequences correspond to the number and sizes of a truly random sequence

    Args:    name: path .json file

    Returns:
             P-value is the probability that the generator
             produces values comparable to the reference
    """
    n = len(name)
    prop_units = name.count("1")/n
    if abs(prop_units - 0.5) >= 2 / math.sqrt(n):
        return 0
    v = sum(0 if name[i] == name[i + 1] else 1 for i in range(n - 1))
    return math.erfc(abs(v - 2 * n * prop_units * (1 - prop_units)) /
                    (2 * math.sqrt(2 * n * prop_units * (1 - prop_units))))


def main() -> None:
    name = get_json(path)["java"]
    frequency_bitwise_test(name)
    identical_consecutive_bits_test(name)


if __name__ == "__main__":
    main()
