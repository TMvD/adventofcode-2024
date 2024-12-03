import pytest

from adventofcode.day03 import (
    execute_instructions,
    execute_operation,
    extract_instructions,
)


@pytest.mark.parametrize(
    "pattern, instructions, expected",
    [
        [
            r"mul\(\d+,\d+\)",
            ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"],
            ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"],
        ],
        [
            r"(mul\(\d+,\d+\)|do\(\)|don\'t\(\))",
            [
                "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
            ],
            ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"],
        ],
    ],
)
def test_parse_instructions(pattern, instructions, expected):
    assert extract_instructions(instructions, pattern) == expected


def test_execute_operation():
    operator, operand1, operand2 = "mul", 2, 4
    assert execute_operation(operator, operand1, operand2) == 8


@pytest.mark.parametrize(
    "instructions, expected",
    [
        [["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"], 161],
        [["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"], 48],
    ],
)
def test_execute_instructions(instructions, expected):
    assert execute_instructions(instructions) == expected
