from collections import deque


def main():
    with open("./data/data_day10.txt", "r", encoding="utf-8") as file:
        map = file.read().splitlines()

    map = parse_map(map)
    scores = sum_trailhead_scores(map)
    print("Sum trailhead scores:", scores)


def parse_map(map: list[str]) -> list[list[int]]:
    return [[int(height) if height.isnumeric() else 0 for height in row] for row in map]


def sum_trailhead_scores(map: list[list[int]]):
    return sum(
        breadth_first_search(map, (x, y))
        for y, row in enumerate(map)
        for x, height in enumerate(row)
        if height == 0
    )


def breadth_first_search(map: list[list[int]], start_coordinates: tuple[int, int]):
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))

    queue = deque([start_coordinates])
    visited = set([start_coordinates])
    nine_count = 0

    while queue:
        x, y = queue.popleft()

        height = map[y][x]
        if height == 9:
            nine_count += 1

        for dx, dy in directions:
            xdx, ydy = x + dx, y + dy
            coordinates = (xdx, ydy)

            if validate_coordinates(map, coordinates) and coordinates not in visited:
                if height + 1 == map[ydy][xdx]:
                    queue.append(coordinates)
                    visited.add(coordinates)
    return nine_count


def validate_coordinates(map: list[list[int]], coordinates: tuple[int, int]) -> bool:
    x, y = coordinates
    y_len = len(map)
    x_len = len(map[0])

    return 0 <= x < x_len and 0 <= y < y_len


if __name__ == "__main__":
    main()
