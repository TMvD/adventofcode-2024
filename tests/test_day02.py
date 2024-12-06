import pytest

from adventofcode.day02 import (
    check_dampened_report_safety,
    check_report_safety,
    count_safe_reports,
)


@pytest.mark.parametrize(
    "input, expected",
    [
        [[7, 6, 4, 2, 1], True],
        [[1, 2, 7, 8, 9], False],
        [[9, 7, 6, 2, 1], False],
        [[1, 3, 2, 4, 5], False],
        [[8, 6, 4, 4, 1], False],
        [[1, 3, 6, 7, 9], True],
    ],
)
def test_check_report_safety(input, expected):
    # True == safe
    # False == unsafe
    assert check_report_safety(input) == expected


def test_count_safe_reports():
    reports = [True, False, False, False, True]
    assert count_safe_reports(reports) == 2


@pytest.mark.parametrize(
    "input, expected",
    [
        [[7, 6, 4, 2, 1], True],
        [[1, 2, 7, 8, 9], False],
        [[9, 7, 6, 2, 1], False],
        [[1, 3, 2, 4, 5], True],
        [[8, 6, 4, 4, 1], True],
        [[1, 3, 6, 7, 9], True],
    ],
)
def test_check_dampened_report_safety(input, expected):
    assert check_dampened_report_safety(input) == expected
