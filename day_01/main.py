def part_one(file: str) -> int:
    elves_cals = process_file(file)
    # print(elves_cals)
    cal_sums = [sum(elf_cals) for elf_cals in elves_cals]
    return max(cal_sums)


def process_file(file: str) -> list[list[int]]:
    with open(file, 'r') as f:
        elves = f.read().split("\n\n")
        return [list(map(int, elf.split())) for elf in elves]


def part_two(file: str) -> int:
    elves_cals = process_file(file)
    cal_sums = [sum(elf_cals) for elf_cals in elves_cals]
    cal_sums.sort(reverse=True)
    return sum(cal_sums[0:3])


if __name__ == "__main__":
    input_path = "./day_01/input.txt"
    print("==== PART 1 ====")
    print(part_one(input_path))
    print("==== PART 2 ====")
    print(part_two(input_path))
