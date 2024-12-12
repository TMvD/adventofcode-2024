from collections import Counter


def main(blinks: int):
    with open("./data/data_day11.txt", "r", encoding="utf-8") as file:
        stones = file.readline().strip()

    stones = [int(stone) for stone in stones.split(" ")]
    stone_count = count_stones(stones, blinks)
    print(f"Stone count {blinks} blinks: {stone_count}")


def count_stones(stones: list[int], blinks: int) -> int:
    stone_count = Counter(stones)
    for _ in range(blinks):
        stone_count = blink(stone_count)
    return sum(stone_count.values())


def blink(stone_count: dict[int, int]) -> dict[int, int]:
    new_stone_count = Counter()
    for stone, count in stone_count.items():
        if stone == 0:
            new_stone_count[1] += count
        elif is_even_digits(stone):
            left, right = split_stone(stone)
            new_stone_count[left] += count
            new_stone_count[right] += count
        else:
            new_stone = stone * 2024
            new_stone_count[new_stone] += count
    return new_stone_count


def is_even_digits(number: int) -> bool:
    return not (len(str(number)) % 2)


def split_stone(number: int) -> tuple[int, int]:
    number_str = str(number)
    midpoint = int(len(number_str) / 2)
    return int(number_str[:midpoint]), int(number_str[midpoint:])


if __name__ == "__main__":
    main(25)
    main(75)
