from day2.part1 import parse_line, ids_of_possible_games


def test_parse_line():
    assert parse_line("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green") == [
        {
            "blue": 3,
            "red": 4,
        },
        {
            "red": 1,
            "green": 2,
            "blue": 6,
        },
        {
            "green": 2,
        },
    ]


def test_sum_of_indexes_of_possible_games():
    assert ids_of_possible_games([[{"blue": 18}]], bag_content={"blue": 3}) == [1]


def test_sum_of_indexes_of_possible_games_with_missing_color():
    assert ids_of_possible_games([[{"red": 18}]], bag_content={"blue": 3}) == [1]


def test_main():
    test_lines = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    games = [parse_line(line) for line in test_lines]
    result = ids_of_possible_games(
        games,
        {
            "red": 12,
            "green": 13,
            "blue": 14,
        },
    )
    assert result == [1, 2, 5]
