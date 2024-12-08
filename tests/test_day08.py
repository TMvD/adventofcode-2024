import pytest

from adventofcode.day08 import (
    Coordinates,
    count_antinodes,
    fetch_antenna_coordinates,
    fetch_antinode_coordinates,
    validate_coordinates,
)


@pytest.fixture
def map():
    return [
        "............",
        "........0...",
        ".....0......",
        ".......0....",
        "....0.......",
        "......A.....",
        "............",
        "............",
        "........A...",
        ".........A..",
        "............",
        "............",
    ]


def test_count_antinodes(map):
    assert count_antinodes(map) == 14


def test_fetch_antenna_coordinates(map: list[str]):
    expected = {
        "0": [
            Coordinates(8, 1),
            Coordinates(5, 2),
            Coordinates(7, 3),
            Coordinates(4, 4),
        ],
        "A": [Coordinates(6, 5), Coordinates(8, 8), Coordinates(9, 9)],
    }
    assert fetch_antenna_coordinates(map) == expected


@pytest.mark.parametrize(
    "antenna_coordinates, expected",
    [
        (
            [
                Coordinates(8, 1),
                Coordinates(5, 2),
                Coordinates(7, 3),
                Coordinates(4, 4),
            ],
            {
                Coordinates(6, 0),
                Coordinates(11, 0),
                Coordinates(3, 1),
                Coordinates(10, 2),
                Coordinates(2, 3),
                Coordinates(9, 4),
                Coordinates(1, 5),
                Coordinates(6, 5),
                Coordinates(3, 6),
                Coordinates(0, 7),
            },
        ),
        (
            [Coordinates(6, 5), Coordinates(8, 8), Coordinates(9, 9)],
            {
                Coordinates(3, 1),
                Coordinates(4, 2),
                Coordinates(7, 7),
                Coordinates(10, 10),
                Coordinates(10, 11),
            },
        ),
    ],
)
def test_fetch_antinode_coordinates(map, antenna_coordinates, expected):
    assert fetch_antinode_coordinates(map, antenna_coordinates) == expected


@pytest.mark.parametrize(
    "coordinates1, coordinates2, expected",
    [
        (Coordinates(0, 0), Coordinates(3, 3), Coordinates(3, 3)),
        (Coordinates(3, 4), Coordinates(4, 5), Coordinates(7, 9)),
        (Coordinates(4, 5), Coordinates(3, 4), Coordinates(7, 9)),
    ],
)
def test_add_coordinates(coordinates1, coordinates2, expected):
    assert coordinates1 + coordinates2 == expected


@pytest.mark.parametrize(
    "coordinates1, coordinates2, expected",
    [
        (Coordinates(0, 0), Coordinates(3, 3), Coordinates(-3, -3)),
        (Coordinates(3, 4), Coordinates(4, 5), Coordinates(-1, -1)),
        (Coordinates(4, 5), Coordinates(3, 4), Coordinates(1, 1)),
    ],
)
def test_sub_coordinates(coordinates1, coordinates2, expected):
    assert coordinates1 - coordinates2 == expected


@pytest.mark.parametrize(
    "coordinates, expected",
    [
        (Coordinates(-3, -3), Coordinates(3, 3)),
        (Coordinates(-1, 1), Coordinates(1, 1)),
        (Coordinates(1, 1), Coordinates(1, 1)),
        (Coordinates(4, -2), Coordinates(4, 2)),
        (Coordinates(0, 0), Coordinates(0, 0)),
    ],
)
def test_abs_coordinates(coordinates, expected):
    assert abs(coordinates) == expected


@pytest.mark.parametrize(
    "coordinates, expected",
    [
        (Coordinates(-3, -3), False),
        (Coordinates(-1, 1), False),
        (Coordinates(4, -2), False),
        (Coordinates(0, 0), True),
        (Coordinates(2, 2), True),
        (Coordinates(11, 11), True),
        (Coordinates(12, 12), False),
    ],
)
def test_validate_coordinates(map, coordinates, expected):
    assert validate_coordinates(map, coordinates) == expected
