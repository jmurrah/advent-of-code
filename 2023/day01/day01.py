from collections import defaultdict


def find_number(line: str):
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    locations = defaultdict(str)

    for i in range(len(line)):
        for j in range(1, 6):
            substring = line[i : i + j]
            if substring in digits:
                locations[i] = digits[substring]
                break
            elif substring.isdigit():
                locations[i] = substring
                break

    return int(locations[min(locations)] + locations[max(locations)])


if __name__ == "__main__":

    with open("input.txt") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        total += find_number(line)

    print(total)
