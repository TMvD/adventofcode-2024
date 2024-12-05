import pytest

from adventofcode.day05 import (
    check_order,
    fix_order,
    parse_rules,
    sum_pages,
    sum_reordered_pages,
)


@pytest.mark.parametrize(
    "update, expected",
    [
        [[75, 47, 61, 53, 29], True],
        [[97, 61, 53, 29, 13], True],
        [[75, 29, 13], True],
        [[75, 97, 47, 61, 53], False],
        [[61, 13, 29], False],
        [[97, 13, 75, 29, 47], False],
    ],
)
def test_check_order(update, expected):
    rules = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
    ]
    rules = parse_rules(rules)
    assert check_order(update, rules) == expected


def test_sum_pages():
    updates = [
        [75, 47, 61, 53, 29],
        [97, 61, 53, 29, 13],
        [75, 29, 13],
    ]
    rules = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
    ]
    rules = parse_rules(rules)
    assert sum_pages(updates, rules) == 143


@pytest.mark.parametrize(
    "pages, expected",
    [
        [[75, 97, 47, 61, 53], [97, 75, 47, 61, 53]],
        [[61, 13, 29], [61, 29, 13]],
        [[97, 13, 75, 29, 47], [97, 75, 47, 29, 13]],
    ],
)
def test_fix_order(pages, expected):
    rules = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
    ]
    rules = parse_rules(rules)
    assert fix_order(pages, rules) == expected


def test_sum_reordered_pages():
    updates = [
        [75, 47, 61, 53, 29],  # True
        [75, 97, 47, 61, 53],
        [61, 13, 29],
        [97, 13, 75, 29, 47],
    ]
    rules = [
        "47|53",
        "97|13",
        "97|61",
        "97|47",
        "75|29",
        "61|13",
        "75|53",
        "29|13",
        "97|29",
        "53|29",
        "61|53",
        "97|53",
        "61|29",
        "47|13",
        "75|47",
        "97|75",
        "47|61",
        "75|61",
        "47|29",
        "75|13",
        "53|13",
    ]
    rules = parse_rules(rules)
    assert sum_reordered_pages(updates, rules) == 123
