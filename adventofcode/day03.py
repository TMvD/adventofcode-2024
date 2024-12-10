import re


def main():
    with open("./data/data_day03.txt", "r", encoding="utf-8") as file:
        data = file.read().splitlines()

    multiply_pattern = r"mul\(\d+,\d+\)"
    multiply_instructions = extract_instructions(data, multiply_pattern)
    sum_multiply_instructions = execute_instructions(multiply_instructions)
    print("Sum of multiply instructions: ", sum_multiply_instructions)

    conditional_pattern = r"(mul\(\d+,\d+\)|do\(\)|don\'t\(\))"
    conditional_instructions = extract_instructions(data, conditional_pattern)
    sum_conditional_instructions = execute_instructions(conditional_instructions)
    print("Sum of conditional multiply instructions: ", sum_conditional_instructions)


def extract_instructions(instructions: list[str], pattern: str):
    matches = []
    for text in instructions:
        matches.extend(re.findall(pattern, text))
    return matches


def execute_instructions(instructions: list[str]):
    do = True
    pattern = r"(\w+)\((\d+),(\d+)\)"
    total = 0
    for instruction in instructions:
        if instruction == "do()":
            do = True
        elif instruction == "don't()":
            do = False
        elif do:
            matches = re.search(pattern, instruction)
            operator, operand1, operand2 = matches.groups()
            total += execute_operation(operator, operand1, operand2)
    return total


def execute_operation(operator: str, operand1: str | int, operand2: str | int) -> int:
    match operator:
        case "mul":
            return int(operand1) * int(operand2)
        case _:
            print(f"Unknown operator: {operator}")
            return 0


if __name__ == "__main__":
    main()
