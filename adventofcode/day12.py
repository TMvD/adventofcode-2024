from collections import deque
from dataclasses import dataclass, field


class Coordinates:
    def __init__(self, x: int, y: int):
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


@dataclass
class Region:
    area: int
    region: int
    visited: set[Coordinates] = field(default_factory=set)


def main():
    with open("./data/data_day12.txt", "r", encoding="utf-8") as file:
        map = file.read().splitlines()

    total_price = get_total_price(map)
    print(f"Total price: {total_price}")


def get_total_price(map: list[str]):
    visited: set[Coordinates] = set()
    total_price = 0

    for y, row in enumerate(map):
        for x, plot in enumerate(row):
            if (coordinates := Coordinates(x, y)) not in visited:
                total_price += get_region_price(map, coordinates, plot, visited)
    return total_price


def get_region_price(
    map: list[str], start_coordinates: Coordinates, plot: str, visited: set[Coordinates]
):
    directions = [
        Coordinates(-1, 0),
        Coordinates(1, 0),
        Coordinates(0, -1),
        Coordinates(0, 1),
    ]
    area = 0
    perimeter = 0

    queue = deque([start_coordinates])
    while queue:
        coordinates = queue.popleft()
        if coordinates in visited:
            continue
        visited.add(coordinates)
        area += 1

        for direction in directions:
            dcoordinates = coordinates + direction
            if not validate_coordinates(map, dcoordinates):
                perimeter += 1
                continue

            dplot = map[dcoordinates.y][dcoordinates.x]
            if dcoordinates in visited and dplot == plot:
                continue

            if dplot == plot:
                queue.append(dcoordinates)
            else:
                perimeter += 1

    return area * perimeter


def validate_coordinates(map: list[str], coordinates: Coordinates) -> bool:
    x, y = coordinates.x, coordinates.y
    y_len = len(map)
    x_len = len(map[0])

    return 0 <= x < x_len and 0 <= y < y_len


if __name__ == "__main__":
    main()
