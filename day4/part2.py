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
    n_cards = {i: 1 for i in range(len(input))}
    for i_card in n_cards.keys():
        line = input[i_card]
        winning_numbers, my_numbers = parse_line(line)
        n_winning = len(winning_numbers.intersection(my_numbers))
        won_cards = list(range(i_card + 1, i_card + 1 + n_winning))
        for id_won in won_cards:
            n_cards[id_won] += n_cards[i_card]
    return sum(n_cards.values())


if __name__ == "__main__":
    print(main())
