import json
import math
import mpmath

from typing import Dict

from const import PATH, PI


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
             float: P-value is the probability that the
                    generator produces values comparable
                    to the reference
    """
    s = abs(sum(1 if i == "1" else -1 for i in name)) / math.sqrt(len(name))
    return math.erfc(s / math.sqrt(2))


def identical_consecutive_bits_test(name: str) -> float:
    """
    The function searches for all sequences of identical bits,
    and then analyzes how much the number and sizes of these
    sequences correspond to the number and sizes of a truly random sequence

    Args:    name: path .json file

    Returns:
             p_value: P-value is the probability that the generator
                    produces values comparable to the reference
    """
    n = len(name)
    units = name.count("1") / n
    if abs(units - 0.5) >= 2 / math.sqrt(n):
        return 0
    v = sum(0 if name[i] == name[i + 1] else 1 for i in range(n - 1))
    p_value = math.erfc(abs(v - 2 * n * units * (1 - units)) /
                       (2 * math.sqrt(2 * n) * units * (1 - units)))
    return p_value


def max_sequence_units(name: str) -> int:
    """
    The function searches for the maximum length of a
    sequence of consecutive units

    Args:
             name: path .json file
    Returns:
             maximum: longest sequence units
    """
    maximum = 0
    count = 0
    for i in name:
        if i == "1":
            count += 1
            maximum = max(maximum, count)
        else:
            maximum = max(maximum, count)
            count = 0
    return maximum


def longest_sequence_units_test(name: str) -> float:
    """
    In this test, the longest row of units inside a block
    with a length of m bits is determined

    Args:
             name: path .json file
    Returns:
             float: P-value
    """
    n = len(name)
    m = 8
    count_max = []
    for i in range(0, n, m):
        block_len = count_max.append(max_sequence_units(name[i: i + 8]))
    v1 = count_max.count(0) + count_max.count(1)
    v2 = count_max.count(2)
    v3 = count_max.count(3)
    v4 = len(count_max) - v1 - v2 - v3
    v = [v1, v2, v3, v4]

    hi = sum((v[i] - 16 * PI[i]) ** 2 / (16 * PI[i]) for i in range(4))
    return mpmath.gammainc(1.5, hi / 2)


def main() -> None:
    name = get_json(PATH)["java"]
    frequency_bitwise_test(name)
    identical_consecutive_bits_test(name)
    longest_sequence_units_test(name)


if __name__ == "__main__":
    main()
