def main():
    with open("./data/data_day01.txt", "r", encoding="utf-8") as file:
        data = file.read().splitlines()
    ids1, ids2 = parse_data(data)
    print("Total distance: ", calculate_total_distance(ids1, ids2))
    print("Similarity score: ", calculate_similarity_score(ids1, ids2))


def parse_data(data: list[str]) -> tuple[list[int], list[int]]:
    location_ids_1: list[int] = []
    location_ids_2: list[int] = []

    for line in data:
        a, b = line.split("   ")
        location_ids_1.append(int(a))
        location_ids_2.append(int(b))

    return location_ids_1, location_ids_2


def calculate_total_distance(
    location_ids_1: list[int], location_ids_2: list[int]
) -> int:
    location_ids_1.sort()
    location_ids_2.sort()
    return sum([abs(id1 - id2) for id1, id2 in zip(location_ids_1, location_ids_2)])


def calculate_similarity_score(list1: list[int], list2: list[int]) -> int:
    """
    for i in list1:
        n = list2.count(i)
        total += (i * n)
    return total
    """
    return sum([a * list2.count(a) for a in list1])


main()
