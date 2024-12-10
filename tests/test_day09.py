import pytest

from adventofcode.day09 import (
    calculate_checksum,
    decode_diskmap,
    defragment,
    defragment_file,
    defragment_whole_files,
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


@pytest.mark.parametrize(
    "blocks, expected",
    [
        (
            list("00...111...2...333.44.5555.6666.777.888899"),
            list("00992111777.44.333....5555.6666.....8888.."),
        )
    ],
)
def test_defragment_whole(blocks, expected):
    assert defragment_whole_files(blocks) == expected


@pytest.mark.parametrize(
    "blocks, file_id, expected",
    [
        (
            list("00...111...2...333.44.5555.6666.777.888899"),
            9,
            list("0099.111...2...333.44.5555.6666.777.8888.."),
        ),
        (
            list("0099.111777244.333....5555.6666.....8888.."),
            2,
            list("00992111777.44.333....5555.6666.....8888.."),
        ),
    ],
)
def test_defragment_file(blocks, file_id, expected):
    assert defragment_file(blocks, file_id) == expected


@pytest.mark.parametrize(
    "blocks, expected",
    [
        (list("0099811188827773336446555566.............."), 1928),
        (list("00992111777.44.333....5555.6666.....8888.."), 2858),
    ],
)
def test_calculate_checksum(blocks, expected):
    assert calculate_checksum(blocks) == expected
