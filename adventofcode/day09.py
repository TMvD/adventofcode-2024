def main():
    with open("./data/data_day09.txt", "r", encoding="utf-8") as file:
        map = file.read()

    blocks = decode_diskmap(map)
    blocks = defragment(blocks)
    checksum = calculate_checksum(blocks)
    print("Checksum:", checksum)


def decode_diskmap(diskmap: str):
    diskmap = diskmap.replace("\n", "")
    blocks: list[str] = []
    id = 0

    for i, mapped in enumerate(diskmap):
        if not (i % 2):
            blocks += int(mapped) * [str(id)]
            id += 1
        else:
            blocks += int(mapped) * ["."]
    return blocks


def defragment(blocks: list[str]):
    for i, block in enumerate(blocks):
        if block != ".":
            continue
        if i < (j := find_last_block_index(blocks)):
            blocks[i], blocks[j] = blocks[j], blocks[i]
    return blocks


def find_last_block_index(blocks: list[str]):
    max_i = len(blocks) - 1
    for i in range(max_i, -1, -1):
        if blocks[i] != ".":
            return i
    raise ValueError


def calculate_checksum(blocks: list[str]):
    checksum = 0
    for position, file_id in enumerate(blocks):
        if file_id == ".":
            break
        checksum += position * int(file_id)
    return checksum


if __name__ == "__main__":
    main()
