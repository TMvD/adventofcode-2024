import os
from pathlib import Path

import dotenv
import httpx


def main(i: int):
    """Create template files for each day"""
    print(f"Creating files for day {i}")

    Path.touch(Path.cwd() / "adventofcode" / f"day{i:02}.py")
    Path.touch(Path.cwd() / "tests" / f"test_day{i:02}.py")

    save_and_fetch_test_data(i)
    print("Files createad")


def save_and_fetch_test_data(i: int):
    dotenv.load_dotenv()
    sessionToken = os.getenv("AOC_TOKEN")
    url = f"https://adventofcode.com/2024/day/{i}/input"
    headers = {"Cookie": sessionToken}
    response = httpx.get(url, headers=headers)

    try:
        response.raise_for_status()
        with open(
            f"{Path.cwd()}/data/data_day{i:02}.txt", "w", encoding="utf-8"
        ) as file:
            file.write(response.text)
    except httpx.RequestError as e:
        print(f"Error downloading data: {e}")


if __name__ == "__main__":
    main(3)
