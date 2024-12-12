import pytest

from adventofcode.day12 import Coordinates, get_region_price, get_total_price


@pytest.fixture
def large_map():
    return [
        "RRRRIICCFF",
        "RRRRIICCCF",
        "VVRRRCCFFF",
        "VVRCCCJFFF",
        "VVVVCJJCFE",
        "VVIVCCJJEE",
        "VVIIICJJEE",
        "MIIIIIJJEE",
        "MIIISIJEEE",
        "MMMISSJEEE",
    ]


def test_get_total_price(large_map):
    assert get_total_price(large_map) == 1930


@pytest.mark.parametrize(
    "start_coordinates, plot, expected",
    [
        (Coordinates(0, 0), "R", 216),
        (Coordinates(4, 0), "I", 32),
        (Coordinates(6, 0), "C", 392),
        (Coordinates(8, 0), "F", 180),
        (Coordinates(0, 2), "V", 260),
        (Coordinates(6, 3), "J", 220),
        (Coordinates(7, 4), "C", 4),
        (Coordinates(9, 4), "E", 234),
        (Coordinates(2, 5), "I", 308),
        (Coordinates(0, 7), "M", 60),
        (Coordinates(4, 8), "S", 24),
    ],
)
def test_get_region_price(
    large_map, start_coordinates: Coordinates, plot: str, expected: int
):
    assert get_region_price(large_map, start_coordinates, plot, set()) == expected
