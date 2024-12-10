import pytest

from adventofcode.day09 import (
    calculate_checksum,
    decode_diskmap,
    defragment,
    find_last_block_index,
)


@pytest.mark.parametrize(
    "diskmap, expected",
    [
        ("12345", list("0..111....22222")),
        ("90909", list("000000000111111111222222222")),
        ("2333133121414131402", list("00...111...2...333.44.5555.6666.777.888899")),
    ],
)
def test_decode_diskmap(diskmap, expected):
    assert decode_diskmap(diskmap) == expected


@pytest.mark.parametrize(
    "blocks, expected",
    [
        (list("0..111....22222"), list("022111222......")),
        (
            list("00...111...2...333.44.5555.6666.777.888899"),
            list("0099811188827773336446555566.............."),
        ),
    ],
)
def test_defragment(blocks, expected):
    assert defragment(blocks) == expected


@pytest.mark.parametrize(
    "blocks, expected",
    [
        (["1", ".", ".", "."], 0),
        ([".", ".", "9", "."], 2),
        ([".", ".", "9", "8"], 3),
    ],
)
def test_find_last_block_index(blocks, expected):
    assert find_last_block_index(blocks) == expected


def test_calculate_checksum():
    assert (
        calculate_checksum(list("0099811188827773336446555566..............")) == 1928
    )
