import operator


def main():
    with open("./data/data_day09.txt", "r", encoding="utf-8") as file:
        map = file.read()

    blocks = decode_diskmap(map)
    blocks = defragment(blocks)
    checksum = calculate_checksum(blocks)
    print("Checksum:", checksum)

    blocks = decode_diskmap(map)
    blocks = defragment_whole_files(blocks)
    checksum = calculate_checksum(blocks)
    print("Whole file checksum", checksum)


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
            continue
        checksum += position * int(file_id)
    return checksum


def defragment_whole_files(blocks: list[str]):
    file_id = find_max_file_id(blocks)

    for file_id in range(file_id, -1, -1):
        blocks = defragment_file(blocks, file_id)
    return blocks


def defragment_file(blocks: list[str], file_id: int):
    file_start = find_start(blocks, str(file_id))
    file_end = find_end(blocks, str(file_id))
    file_size = file_end - file_start
    empty_blocks = 0

    for i, block in enumerate(blocks):
        if block == ".":
            empty_blocks += 1
        else:
            empty_blocks = 0

        if i > file_start:
            break

        if file_size <= empty_blocks:
            empty_start = i - empty_blocks + 1
            empty_end = empty_start + file_size

            empty_slice = slice(empty_start, empty_end)
            file_slice = slice(file_start, file_end)
            blocks[empty_slice], blocks[file_slice] = (
                blocks[file_slice],
                blocks[empty_slice],
            )
            break
    return blocks


def find_max_file_id(blocks: list[str]) -> int:
    for file_id in reversed(blocks):
        if file_id != ".":
            return int(file_id)
    raise ValueError


def find_start(blocks: list[str], file_id: str):
    return blocks.index(str(file_id))


def find_end(blocks: list[str], file_id: str):
    return len(blocks) - operator.indexOf(reversed(blocks), file_id)


if __name__ == "__main__":
    main()
