import itertools
import re


def main():
    with open("./data/data_day07.txt", "r", encoding="utf-8") as file:
        equations = file.read().splitlines()

    total_calibration = calculate_total_calibrations(equations, ["*", "+"])
    print("Total calibration result:", total_calibration)

    total_calibration = calculate_total_calibrations(equations, ["*", "+", "||"])
    print("Total calibration result:", total_calibration)


def calculate_total_calibrations(equations: list[str], operators: list[str]):
    pattern = r"(\d+)"
    total = 0
    for equation in equations:
        if not (matches := re.findall(pattern, equation)):
            continue
        test_value, *operands = matches
        test_value = int(test_value)
        operands = [int(operand) for operand in operands]
        if validate_calibration(test_value, operands, operators):
            total += test_value
    return total


def validate_calibration(test_value: int, operands: list[int], operators: list[str]):
    operators_amt = len(operands) - 1
    operator_combos = itertools.product(operators, repeat=operators_amt)

    for operator_combo in operator_combos:
        t = operands[0]
        for i, operand in enumerate(operands[1:]):
            match operator_combo[i]:
                case "+":
                    t += operand
                case "*":
                    t *= operand
                case "||":
                    t = int(str(t) + str(operand))
        if t == test_value:
            return True
    return False


if __name__ == "__main__":
    main()
