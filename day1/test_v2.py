from day1.part2 import calibration_value, main


def test_calibration_value_with_two_digits():
    assert calibration_value("1foo2") == 12


def test_calibration_value_with_one_digit():
    assert calibration_value("1foo") == 11


def test_calibration_value_with_three_digits():
    assert calibration_value("1foo2bar3") == 13


def test_calibration_value_with_one_string_digit():
    assert calibration_value("1footwo") == 12


def test_calibration_value_with_two_string_digit():
    assert calibration_value("eightfootwo") == 82


def test_main_v2_gives_right_result():
    assert main() == 55260
