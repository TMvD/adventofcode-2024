from collections import defaultdict


def main():
    with open("./data/data_day05a.txt", "r", encoding="utf-8") as file:
        raw_rules = file.read().splitlines()

    rules = parse_rules(raw_rules)

    with open("./data/data_day05b.txt", "r", encoding="utf-8") as file:
        raw_updates = file.read().splitlines()

    updates = parse_updates(raw_updates)

    pages_sum = sum_pages(updates, rules)
    print("Sum of middle page numbers:", pages_sum)

    fixed_pages_sum = sum_reordered_pages(updates, rules)
    print("Sum of middle page numbers of fixed updates:", fixed_pages_sum)


def parse_rules(raw_rules: list[str]):
    rules = defaultdict(set)
    for rule in raw_rules:
        k, v = rule.split("|")
        rules[int(k)].add(int(v))
    return rules


def parse_updates(raw_updates: list[str]):
    updates = []
    for update in raw_updates:
        pages = update.split(",")
        pages = [int(p) for p in pages]
        updates.append(pages)
    return updates


def sum_pages(updates: list[list[int]], rules: dict[int, set]):
    pages_sum = 0
    for update in updates:
        if check_order(update, rules):
            pages_sum += get_middle_element(update)
    return pages_sum


def check_order(update_pages: list[int], rules: dict[int, set]):
    remaining_pages = set(update_pages)
    for page in update_pages:
        remaining_pages.remove(page)
        if not remaining_pages.issubset(rules[page]):
            return False
    return True


def sum_reordered_pages(updates: list[list[int]], rules: dict[int, set]):
    pages_sum = 0
    for update in updates:
        if not check_order(update, rules):
            update = fix_order(update, rules)
            pages_sum += get_middle_element(update)
    return pages_sum


def fix_order(pages: list[int], rules: dict[int, set]):
    new_pages = []
    remaining_pages = set(pages)
    while pages:
        page = pages.pop(0)
        remaining_pages.remove(page)
        if remaining_pages.issubset(rules[page]):
            new_pages.append(page)
        else:
            pages.append(page)
            remaining_pages.add(page)
    return new_pages


def get_middle_element(lst: list):
    return lst[len(lst) // 2]


if __name__ == "__main__":
    main()
