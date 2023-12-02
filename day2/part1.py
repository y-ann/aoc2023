def preprocess_lines() -> list[str]:
    with open("./input.txt") as f:
        input = f.readlines()
    # Remove newline character
    return [line[:-1] for line in input]


def parse_line(line: str) -> list[dict[str, int]]:
    result = []
    for tirage_str in line.split(":")[1].strip().split(";"):
        tirage_str = tirage_str.strip()
        tirage_list = tirage_str.split(",")
        tirage_dict = {}
        for color_count_str in tirage_list:
            color_count_str = color_count_str.strip()
            color_count_list = color_count_str.split()
            color = color_count_list[1]
            count = color_count_list[0]
            tirage_dict[color] = int(count)
        result.append(tirage_dict)
    return result


def ids_of_possible_games(
    games: list[list[dict[str, int]]],
    bag_content: dict[str, int],
) -> list[int]:
    result = []
    for i, game in enumerate(games):
        game_possible = True
        for tirage in game:
            for color, count in tirage.items():
                if count > bag_content.get(color, 0):
                    game_possible = False
        if game_possible:
            result.append(i + 1)
    return result


def main():
    lines = preprocess_lines()
    games = [parse_line(line) for line in lines]
    ids = ids_of_possible_games(
        games,
        {
            "red": 12,
            "green": 13,
            "blue": 14,
        },
    )
    return sum(ids)


if __name__ == "__main__":
    print(main())
