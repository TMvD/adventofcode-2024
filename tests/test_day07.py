import pytest

from adventofcode.day07 import calculate_total_calibrations, validate_calibration


@pytest.mark.parametrize(
    "equations, operators, expected",
    [
        (
            [
                "190: 10 19",
                "3267: 81 40 27",
                "83: 17 5",
                "156: 15 6",
                "7290: 6 8 6 15",
                "161011: 16 10 13",
                "192: 17 8 14",
                "21037: 9 7 18 13",
                "292: 11 6 16 20",
            ],
            ["*", "+"],
            3749,
        ),
        (
            [
                "190: 10 19",
                "3267: 81 40 27",
                "83: 17 5",
                "156: 15 6",
                "7290: 6 8 6 15",
                "161011: 16 10 13",
                "192: 17 8 14",
                "21037: 9 7 18 13",
                "292: 11 6 16 20",
            ],
            ["*", "+", "||"],
            11387,
        ),
    ],
)
def test_calculate_total_calibrations(equations, operators, expected):
    assert calculate_total_calibrations(equations, operators) == expected


@pytest.mark.parametrize(
    "test_value, operands, operators, expected",
    [
        (190, [10, 19], ["*", "+"], True),
        (3267, [81, 40, 27], ["*", "+"], True),
        (83, [17, 5], ["*", "+"], False),
        (156, [15, 6], ["*", "+"], False),
        (7290, [6, 8, 6, 15], ["*", "+"], False),
        (161011, [16, 10, 13], ["*", "+"], False),
        (192, [17, 8, 14], ["*", "+"], False),
        (21037, [9, 7, 18, 13], ["*", "+"], False),
        (292, [11, 6, 16, 20], ["*", "+"], True),
        (156, [15, 6], ["*", "+", "||"], True),
        (7290, [6, 8, 6, 15], ["*", "+", "||"], True),
        (192, [17, 8, 14], ["*", "+", "||"], True),
    ],
)
def test_validate_calibration(test_value, operands, operators, expected):
    assert validate_calibration(test_value, operands, operators) == expected
