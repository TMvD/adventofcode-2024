def main():
    with open("./data/data_day04.txt", "r", encoding="utf-8") as file:
        data = file.read().splitlines()

    count = check_xmas_occurrences(data)
    print("XMAS occurences: ", count)

    count = check_x_mas_occurrences(data)
    print("X-MAS occurences: ", count)


def check_xmas_occurrences(grid: list[str]):
    directions = [
        (-1, -1),  # nw
        (-1, 0),  # n
        (-1, 1),  # ne
        (0, -1),  # w
        # (0, 0),   # center
        (0, 1),  # e
        (1, -1),  # sw
        (1, 0),  # s
        (1, 1),  # se
    ]

    y_len = len(grid)
    x_len = len(grid[0])

    occurrence_count = 0

    for y in range(y_len):
        for x in range(x_len):
            for dx, dy in directions:
                if check_xmas_direction(
                    grid=grid,
                    word="XMAS",
                    x=x,
                    y=y,
                    dx=dx,
                    dy=dy,
                    x_len=x_len,
                    y_len=y_len,
                ):
                    occurrence_count += 1
    return occurrence_count


def check_xmas_direction(
    grid: list[str], word: str, y: int, x: int, dy: int, dx: int, y_len: int, x_len: int
):
    for i, letter in enumerate(word):
        new_y = y + i * dy
        new_x = x + i * dx

        if new_y < 0 or new_y >= y_len:
            return False
        if new_x < 0 or new_x >= x_len:
            return False
        if grid[new_y][new_x] != letter:
            return False
    return True


def check_x_mas_occurrences(grid: list[str]):
    y_len = len(grid)
    x_len = len(grid[0])

    occurrence_count = 0

    for y in range(y_len):
        for x in range(x_len):
            if check_x_mas(
                grid=grid,
                x=x,
                y=y,
                x_len=x_len,
                y_len=y_len,
            ):
                occurrence_count += 1
    return occurrence_count


def check_x_mas(grid: list[str], y: int, x: int, y_len: int, x_len: int):
    directions = [
        (-1, -1),  # nw
        (-1, 1),  # ne
        (1, -1),  # sw
        (1, 1),  # se
    ]

    if x < 1 or x >= x_len - 1:
        return False
    if y < 1 or y >= y_len - 1:
        return False
    if grid[y][x] != "A":
        return False
    # print(x, y)

    directions = [
        (-1, -1),  # nw
        (-1, 1),  # ne
        (1, -1),  # sw
        (1, 1),  # se
    ]

    for dx, dy in directions:
        if (
            grid[y + dy][x + dx] == "M"
            and grid[y + dy][x - dx] == "M"
            and grid[y - dy][x + dx] == "S"
            and grid[y - dy][x - dx] == "S"
            or grid[y + dy][x + dx] == "M"
            and grid[y + dy][x - dx] == "S"
            and grid[y - dy][x + dx] == "M"
            and grid[y - dy][x - dx] == "S"
        ):
            return True
    return False


if __name__ == "__main__":
    main()
