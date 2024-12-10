from collections import deque


def main():
    with open("./data/data_day10.txt", "r", encoding="utf-8") as file:
        map = file.read().splitlines()

    map = parse_map(map)
    score = sum_trailhead_scores(map)
    print("Sum trailhead scores:", score)

    rating = sum_trailhead_ratings(map)
    print("Sum trailhead ratings:", rating)


def parse_map(map: list[str]) -> list[list[int]]:
    return [
        [int(height) if height.isnumeric() else -1 for height in row] for row in map
    ]


def sum_trailhead_scores(map: list[list[int]]):
    return sum(
        get_trailhead_score(map, (x, y))
        for y, row in enumerate(map)
        for x, height in enumerate(row)
        if height == 0
    )


def get_trailhead_score(map: list[list[int]], start_coordinates: tuple[int, int]):
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


def sum_trailhead_ratings(map: list[list[int]]):
    return sum(
        get_trailhead_rating(map, (x, y))
        for y, row in enumerate(map)
        for x, height in enumerate(row)
        if height == 0
    )


def get_trailhead_rating(
    map: list[list[int]],
    start_coordinates: tuple[int, int],
) -> int:
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    visited = set([start_coordinates])
    trail_count = 0
    x, y = start_coordinates
    height = map[y][x]

    if height == 9:
        return 1

    for dx, dy in directions:
        xdx, ydy = x + dx, y + dy
        coordinates = (xdx, ydy)

        if validate_coordinates(map, coordinates) and coordinates not in visited:
            if height + 1 == map[ydy][xdx]:
                trail_count += get_trailhead_rating(map, (xdx, ydy))
                visited.add(coordinates)
    return trail_count


if __name__ == "__main__":
    main()
