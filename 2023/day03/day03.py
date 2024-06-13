def get_numbers(data, indicies) -> tuple[int, int, int]:
    numbers = []

    for index in indicies:
        i, j = index
        while j >= 0 and j < len(data[i]) and data[i][j].isdigit():
            j -= 1
        j += 1

        number, start = "", j
        while data[i][j].isdigit():
            number += data[i][j]
            j += 1

        numbers.append((start, i, int(number)))

    return numbers


def get_adjacent_digit_indicies(data, memory, x, y):
    if (x, y) in memory:
        return memory[(x, y)]

    indicies = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if data[x + i][y + j].isdigit():
                indicies.append((x + i, y + j))

    memory[(x, y)] = indicies
    return indicies


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.readlines()

    numbers, memory = [], {}

    for i, line in enumerate(data):
        for j, character in enumerate(line.strip()):
            if not character.isdigit() and character != ".":
                numbers.extend(
                    get_numbers(data, get_adjacent_digit_indicies(data, memory, i, j))
                )

    print(sum([number[-1] for number in set(numbers)]))
