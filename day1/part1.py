def preprocess_lines() -> list[str]:
    with open("./input.txt") as f:
        input = f.readlines()
    # Remove newline character
    return [line[:-1] for line in input]


def calibration_value(line: str) -> int:
    first_integer = None
    last_integer = None
    for char in line:
        try:
            integer = int(char)
            if first_integer is None:
                first_integer = integer
            last_integer = integer
        except ValueError:
            pass
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
