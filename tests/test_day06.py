import pytest

from adventofcode.day06 import (
    count_distinct_positions,
    count_obstruction_positions,
    find_start,
    obstruct_coordinate,
)


@pytest.fixture
def map():
    return [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]


def test_find_start(map):
    assert find_start(map) == (4, 6, "^")


def test_count_distinct_positions(map):
    assert count_distinct_positions(map) == 41


def test_obstruct_coordinate(map):
    # m = map.copy()
    m = obstruct_coordinate(map, (0, 0))
    assert m[0][0] == "O"


def test_count_obstruction_positions(map):
    assert count_obstruction_positions(map)
