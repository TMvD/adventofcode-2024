from collections import defaultdict
from itertools import combinations
from pprint import pprint


class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinates(self.x - other.x, self.y - other.y)

    def __abs__(self):
        return Coordinates(abs(self.x), abs(self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Coordinates({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def main():
    with open("./data/data_day08.txt", "r", encoding="utf-8") as file:
        map = file.read().splitlines()

    total_antinodes = count_antinodes(map)
    print("Unique antinode locations:", total_antinodes)


def count_antinodes(map: list[str]):
    antenna_coordinates = fetch_antenna_coordinates(map)
    antinode_coordinates = set()

    for coordinates in antenna_coordinates.values():
        antinode_coordinates |= fetch_antinode_coordinates(map, coordinates)
    pprint(antinode_coordinates)
    return len(antinode_coordinates)


def fetch_antenna_coordinates(map: list[str]) -> dict[str, list[Coordinates]]:
    antenna_coordinates = defaultdict(list)
    for y, row in enumerate(map):
        for x, value in enumerate(row):
            if value == ".":
                continue
            antenna_coordinates[value].append(Coordinates(x, y))
    return antenna_coordinates


def fetch_antinode_coordinates(map: list[str], antenna_coordinates: list[Coordinates]):
    coordinate_combos = combinations(antenna_coordinates, 2)
    antinode_coordinates = set()
    for a, b in coordinate_combos:
        distance = a - b
        antinode_1 = a + distance
        antinode_2 = b - distance
        for antinode in (antinode_1, antinode_2):
            if validate_coordinates(map, antinode):
                antinode_coordinates.add(antinode)
    return antinode_coordinates


def validate_coordinates(map: list[str], coordinates):
    return (0 <= coordinates.x < len(map[0])) and (0 <= coordinates.y < len(map))


main()
