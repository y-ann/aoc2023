from day2.part2 import power, fewest_number_of_cubes, parse_line


def test_power():
    assert (
        power(
            {
                "red": 1,
                "green": 2,
                "blue": 6,
            }
        )
        == 12
    )


def test_fewest_number_of_cubes():
    assert fewest_number_of_cubes([{"blue": 18}, {"red": 5, "blue": 2}]) == {
        "red": 5,
        "blue": 18,
    }


def test_main():
    test_lines = [
        "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
    ]
    games = [parse_line(line) for line in test_lines]
    powers = [power(fewest_number_of_cubes(game)) for game in games]
    assert powers == [48, 12, 1560, 630, 36]
