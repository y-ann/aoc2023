from day1.part1 import calibration_value


def test_calibration_value_with_two_digits():
    assert calibration_value("1foo2") == 12


def test_calibration_value_with_one_digit():
    assert calibration_value("1foo") == 11


def test_calibration_value_with_three_digits():
    assert calibration_value("1foo2bar3") == 13
