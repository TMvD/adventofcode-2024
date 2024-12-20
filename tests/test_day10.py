import pytest

from adventofcode.day10 import (
    get_trailhead_score,
    parse_map,
    sum_trailhead_ratings,
    sum_trailhead_scores,
    validate_coordinates,
)


def test_parse_map():
    map = ["012", "234"]
    expected = [[0, 1, 2], [2, 3, 4]]
    assert parse_map(map) == expected


@pytest.mark.parametrize(
    "map, expected",
    [
        (
            [
                "10..9..",
                "2...8..",
                "3...7..",
                "4567654",
                "...8..3",
                "...9..2",
                ".....01",
            ],
            3,
        ),
        (
            [
                "89010123",
                "78121874",
                "87430965",
                "96549874",
                "45678903",
                "32019012",
                "01329801",
                "10456732",
            ],
            36,
        ),
    ],
)
def test_sum_trailhead_scores(map, expected):
    map = parse_map(map)
    assert sum_trailhead_scores(map) == expected


@pytest.mark.parametrize(
    "map, start_coordinates, expected",
    [
        (
            [
                "...0...",
                "...1...",
                "...2...",
                "6543456",
                "7.....7",
                "8.....8",
                "9.....9",
            ],
            (3, 0),
            2,
        ),
        (
            [
                "..90..9",
                "...1.98",
                "...2..7",
                "6543456",
                "765.987",
                "876....",
                "987....",
            ],
            (3, 0),
            4,
        ),
    ],
)
def test_get_trailhead_score(map, start_coordinates, expected):
    map = parse_map(map)
    assert get_trailhead_score(map, start_coordinates) == expected


@pytest.mark.parametrize(
    "map, expected",
    [
        (
            [
                ".....0.",
                "..4321.",
                "..5..2.",
                "..6543.",
                "..7..4.",
                "..8765.",
                "..9....",
            ],
            3,
        ),
        (
            [
                "..90..9",
                "...1.98",
                "...2..7",
                "6543456",
                "765.987",
                "876....",
                "987....",
            ],
            13,
        ),
        (
            [
                "012345",
                "123456",
                "234567",
                "345678",
                "4.6789",
                "56789.",
            ],
            227,
        ),
        (
            [
                "89010123",
                "78121874",
                "87430965",
                "96549874",
                "45678903",
                "32019012",
                "01329801",
                "10456732",
            ],
            81,
        ),
    ],
)
def test_sum_trailhead_ratings(map, expected):
    map = parse_map(map)
    assert sum_trailhead_ratings(map)


@pytest.mark.parametrize(
    "coordinates, expected",
    [
        ((-1, -1), False),
        ((-1, 0), False),
        ((0, -1), False),
        ((0, 0), True),
        ((2, 1), True),
        ((3, 1), False),
        ((3, 2), False),
        ((2, 2), False),
    ],
)
def test_validate_coordinates(coordinates, expected):
    map = parse_map(["012", "234"])
    assert validate_coordinates(map, coordinates) == expected
