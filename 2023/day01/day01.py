def find_number(line: str):
    for character in line:
        if character.isdigit():
            return character


if __name__ == "__main__":

    with open("input.txt") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        total += int(find_number(line) + find_number(line[::-1]))

    print(total)