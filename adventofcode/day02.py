def main():
    with open("./data/data_day02.txt", "r", encoding="utf-8") as file:
        data = file.read().splitlines()
    reports = parse_data(data)

    report_results = [check_report_safety(x) for x in reports]
    print("Safe reports: ", count_safe_reports(report_results))
    dampened_report_results = [check_dampened_report_safety(x) for x in reports]
    print("Dampened safe reports: ", count_safe_reports(dampened_report_results))


def parse_data(reports: list[str]) -> list[list[int]]:
    return [[int(x) for x in report.split()] for report in reports]


def check_report_safety(report: list[int]) -> bool:
    increasing, decreasing = True, True

    for i, x in enumerate(report[1:], start=1):
        current, last = report[i], report[i - 1]
        if current - last == 0 or abs(current - last) > 3:
            return False
        # increasing
        if current > last:
            decreasing = False
        # decreasing
        elif current < last:
            increasing = False
    return increasing or decreasing


def check_dampened_report_safety(report: list[int]) -> bool:
    if check_report_safety(report):
        return True

    for i, _ in enumerate(report):
        report_copy = report.copy()
        report_copy.pop(i)
        if check_report_safety(report_copy):
            return True
    return False


def count_safe_reports(report_results: list[bool]) -> int:
    return report_results.count(True)


if __name__ == "__main__":
    main()
