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


def fewest_number_of_cubes(
    game: list[dict[str, int]],
) -> dict[str, int]:
    result = {}
    for tirage in game:
        for color, count in tirage.items():
            if count > result.get(color, 0):
                result[color] = count
    return result


def power(
    cube_set: dict[str, int],
) -> int:
    result = 1
    for color, count in cube_set.items():
        result *= count
    return result


def main():
    lines = preprocess_lines()
    games = [parse_line(line) for line in lines]
    powers = [power(fewest_number_of_cubes(game)) for game in games]
    return sum(powers)


if __name__ == "__main__":
    print(main())
