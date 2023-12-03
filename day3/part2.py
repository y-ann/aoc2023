from functools import reduce


def preprocess_lines() -> list[str]:
    with open("./day3/input.txt") as f:
        input = f.readlines()
    # Remove newline character
    return [line[:-1] for line in input]


def detect_symbol_positions(input: list[str]) -> list[tuple[int, int]]:
    result = []
    for i, row in enumerate(input):
        for j, char in enumerate(row):
            if char == "*":
                result.append((i, j))
    return result


def detect_numbers(input: list[str]) -> list[tuple[int, int, int, int]]:
    result = []
    for i, row in enumerate(input):
        current_number = ""
        for j, char in enumerate(row):
            if char.isdigit():
                current_number += char
                last_char = j + 1 == len(row)
                if last_char or not row[j + 1].isdigit():
                    result.append(
                        (int(current_number), i, j + 1 - len(current_number), j + 1)
                    )
                    current_number = ""
    return result


def numbers_matching_symbols(numb, symb) -> dict[int, list[int]]:
    result = {}
    for n in numb:
        for symb_index, s in enumerate(symb):
            row_numb = n[1]
            start_numb = n[2]
            end_numb = n[3] - 1
            i_symb, j_symb = s
            if abs(i_symb - row_numb) <= 1 and (
                (start_numb - j_symb) <= 1 and (j_symb - end_numb) <= 1
            ):
                if symb_index in result.keys():
                    result[symb_index].append(n[0])
                else:
                    result[symb_index] = [n[0]]
    return result


def main():
    input = preprocess_lines()
    symbol_positions = detect_symbol_positions(input)
    numbers_positions = detect_numbers(input)
    gears = numbers_matching_symbols(numbers_positions, symbol_positions)
    gears = {
        key: reduce(lambda x, acc: x * acc, number_list, 1)
        for key, number_list in gears.items()
        if len(number_list) == 2
    }
    return sum(list(gears.values()))


if __name__ == "__main__":
    print(main())
