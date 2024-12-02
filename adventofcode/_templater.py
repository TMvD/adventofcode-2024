from pathlib import Path


def main(i: int):
    """Create template files for each day"""
    cwd = Path.cwd()
    Path.touch(cwd / "adventofcode" / f"day{i}.py")
    Path.touch(cwd / "data" / f"data_day{i}.txt")
    Path.touch(cwd / "tests" / f"test_day{i}.py")


if __name__ == "__main__":
    main(1)
