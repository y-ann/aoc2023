from typing import Optional


def preprocess_lines() -> list[str]:
    with open("./1/input.txt") as f:
        input = f.readlines()
    # Remove newline character
    return [line[:-1] for line in input]


DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def int_value(char: str) -> Optional[int]:
    try:
        return int(char)
    except ValueError:
        return None


def lfind_digit(input: str) -> Optional[int]:
    digits = list(DIGITS.keys())
    min_len = 3
    max_len = 5
    for i in range(min_len, max_len + 1):
        substring = input[:i]
        if substring in digits:
            return DIGITS[substring]
    return None


def calibration_value(line: str) -> int:
    first_integer = None
    last_integer = None
    for i, char in enumerate(line):
        int_digit = int_value(char)
        if int_digit is None:
            int_digit = lfind_digit(line[i:])
        if int_digit:
            if first_integer is None:
                first_integer = int_digit
            last_integer = int_digit
    return 10 * first_integer + last_integer


def sum_of_calibration_values(lines: list[str]) -> int:
    values = []
    for line in lines:
        calib_value = calibration_value(line)
        values.append(calib_value)
    return sum(values)


def main():
    lines = preprocess_lines()
    return sum_of_calibration_values(lines)


if __name__ == "__main__":
    print(main())
