class LoopingError(Exception):
    """Current path has already been traversed"""


def main():
    with open("./data/data_day06.txt", "r", encoding="utf-8") as file:
        map = file.read().splitlines()

    distinct_coordinates = count_distinct_positions(map)
    print("Distinct positions:", distinct_coordinates)

    obstruction_coordinates = count_obstruction_positions(map)
    print("Obstruction coordinates:", obstruction_coordinates)


def count_distinct_positions(map: list[str]):
    coordinates = find_start(map)
    route = traverse_map(map, coordinates)
    distinct_coordinates = {(x, y) for x, y, _ in route}
    return len(distinct_coordinates)


def find_start(map: list[str]):
    for y, row in enumerate(map):
        for x, column in enumerate(row):
            if column in "^<>v":
                return (x, y, column)
    raise Exception("Guard not found")


def traverse_map(map: list[str], coordinates: tuple[int, int, str]):
    x, y, direction = coordinates

    route = {coordinates}
    directions = "^>v<"
    direction_mapping = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

    max_x = len(map[0]) - 1
    max_y = len(map) - 1

    while True:
        dx, dy = direction_mapping[direction]
        xdx = x + dx
        ydy = y + dy

        if xdx < 0 or xdx > max_x or ydy < 0 or ydy > max_y:
            return route

        if map[ydy][xdx] in "#O":
            direction = directions[((directions.index(direction) + 1) % 4)]
        else:
            x += dx
            y += dy
        coordinates = (x, y, direction)

        if coordinates in route:
            raise LoopingError

        route.add(coordinates)


def count_obstruction_positions(map):
    start_coordinates = find_start(map)
    route = traverse_map(map, start_coordinates)
    route.remove(start_coordinates)
    distinct_coordinates = {(x, y) for x, y, _ in route}
    loops = 0

    for coordinates in distinct_coordinates:
        m = obstruct_coordinate(map, coordinates)
        try:
            traverse_map(m, start_coordinates)
        except LoopingError:
            loops += 1
    return loops


def obstruct_coordinate(map: list[str], coordinates: tuple[int, int]):
    m = map.copy()
    x, y = coordinates
    row = m[y]
    row = row[:x] + "O" + row[x + 1 :]
    m[y] = row
    return m


main()
