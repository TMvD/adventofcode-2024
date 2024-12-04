import pytest

from adventofcode.day04 import check_x_mas_occurrences, check_xmas_occurrences


def test_check_xmas_occurrences():
    grid = [
        "....XXMAS.",
        ".SAMXMS...",
        "...S..A...",
        "..A.A.MS.X",
        "XMASAMX.MM",
        "X.....XA.A",
        "S.S.S.S.SS",
        ".A.A.A.A.A",
        "..M.M.M.MM",
        ".X.X.XMASX",
    ]
    assert check_xmas_occurrences(grid) == 18


@pytest.mark.parametrize(
    "grid, expected",
    [
        [
            [
                ".M.S......",
                "..A..MSMS.",
                ".M.S.MAA..",
                "..A.ASMSM.",
                ".M.S.M....",
                "..........",
                "S.S.S.S.S.",
                ".A.A.A.A..",
                "M.M.M.M.M.",
                "..........",
            ],
            9,
        ],
        [
            [
                "M.S",
                ".A.",
                "M.S",
            ],
            1,
        ],
    ],
)
def test_check_x_mas_occurrences(grid, expected):
    assert check_x_mas_occurrences(grid) == expected
