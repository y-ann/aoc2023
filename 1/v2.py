from typing import Optional


def preprocess_lines() -> list[str]:
    with open("./1/input.txt") as f:
        input = f.readlines()
    # Remove newline character
    return [line[:-1] for line in input]


DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def calibration_value(line: str) -> int:
    first_integer = None
    last_integer = None
    for k, v in DIGITS.items():
        line = line.replace(k, v)
    for char in line:
        if char.isdigit():
            int_digit = int(char)
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
