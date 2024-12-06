from adventofcode.day01 import calculate_similarity_score, calculate_total_distance


def test_total_distance() -> None:
    location_ids_1: list[int] = [3, 4, 2, 1, 3, 3]
    location_ids_2: list[int] = [4, 3, 5, 3, 9, 3]
    assert calculate_total_distance(location_ids_1, location_ids_2) == 11


def test_similarity_score() -> None:
    list1: list[int] = [3, 4, 2, 1, 3, 3]
    list2: list[int] = [4, 3, 5, 3, 9, 3]
    assert calculate_similarity_score(list1, list2) == 31
