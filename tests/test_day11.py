from collections import Counter

import pytest

from adventofcode.day11 import blink, count_stones, is_even_digits, split_stone


@pytest.mark.parametrize(
    "stones, expected",
    [
        ([0, 1, 10, 99, 999], [1, 2024, 1, 0, 9, 9, 2021976]),
        ([125, 17], [253000, 1, 7]),
        ([253000, 1, 7], [253, 0, 2024, 14168]),
        ([253, 0, 2024, 14168], [512072, 1, 20, 24, 28676032]),
        ([512072, 1, 20, 24, 28676032], [512, 72, 2024, 2, 0, 2, 4, 2867, 6032]),
        (
            [512, 72, 2024, 2, 0, 2, 4, 2867, 6032],
            [1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32],
        ),
        (
            [1036288, 7, 2, 20, 24, 4048, 1, 4048, 8096, 28, 67, 60, 32],
            [
                2097446912,
                14168,
                4048,
                2,
                0,
                2,
                4,
                40,
                48,
                2024,
                40,
                48,
                80,
                96,
                2,
                8,
                6,
                7,
                6,
                0,
                3,
                2,
            ],
        ),
    ],
)
def test_blink(stones, expected):
    stones = Counter(stones)
    expected = Counter(expected)
    assert blink(stones) == expected


@pytest.mark.parametrize(
    "stones, blinks, expected",
    [([125, 17], 6, 22), ([125, 17], 25, 55312)],
)
def test_count_stones(stones, blinks, expected):
    assert count_stones(stones, blinks) == expected


@pytest.mark.parametrize("number, expected", [(111, False), (11, True), (0, False)])
def test_is_even_digits(number, expected):
    assert is_even_digits(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [(17, (1, 7)), (2024, (20, 24)), (512072, (512, 72)), (1000, (10, 0))],
)
def test_split_stone(number, expected):
    assert split_stone(number) == expected
