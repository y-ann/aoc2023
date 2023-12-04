import re


def preprocess_lines() -> list[str]:
    with open("./day4/input.txt") as f:
        input = f.readlines()
    # Remove newline character
    return [line[:-1] for line in input]


def parse_ints(input: str) -> list[int]:
    result = []
    number = ""
    for i, char in enumerate(input):
        if char.isdigit():
            number += char
            if number and (i + 1 == len(input) or not input[i + 1].isdigit()):
                result.append(int(number))
                number = ""
    return result


def parse_line(line: str) -> tuple[set[int], set[int]]:
    line = line.split(":")[1].strip()
    line = line.split("|")
    return set(parse_ints(line[0].strip())), set(parse_ints(line[1].strip()))


def main():
    input = preprocess_lines()
    result = 0
    for line in input:
        winning_numbers, my_numbers = parse_line(line)
        n_winning = len(winning_numbers.intersection(my_numbers))
        if n_winning == 0:
            result += 0
        else:
            result += 2 ** (n_winning - 1)
    return result


if __name__ == "__main__":
    print(main())
