import re


def preprocess_lines() -> list[str]:
    with open("./day3/input.txt") as f:
        input = f.readlines()
    # Remove newline character
    return [line[:-1] for line in input]


def detect_symbol_positions(input: list[str]) -> list[tuple[int, int]]:
    result = []
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if char != "." and not char.isdigit():
                result.append((i, j))
    return result


def detect_numbers(input: list[str]) -> list[tuple[int, int, int, int]]:
    result = []
    for i, row in enumerate(input):
        for match in re.finditer(r"[0-9]*", row):
            start = match.start(0)
            end = match.end(0)
            if start != end:
                number = int(row[start:end])
                result.append((number, i, start, end))
    return result


def numbers_matching_symbols(numb, symb) -> list[int]:
    result = []
    for n in numb:
        for s in symb:
            row_numb = n[1]
            start_numb = n[2]
            end_numb = n[3] - 1
            i_symb, j_symb = s
            if abs(i_symb - row_numb) <= 1 and (
                (start_numb - j_symb) <= 1 and (j_symb - end_numb) <= 1
            ):
                result.append(n[0])
    return result


def main():
    input = preprocess_lines()
    symbol_positions = detect_symbol_positions(input)
    numbers_positions = detect_numbers(input)
    return sum(numbers_matching_symbols(numbers_positions, symbol_positions))


if __name__ == "__main__":
    print(main())
