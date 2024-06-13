def get_adjacent_numbers(
    data: list[str], indicies: list[tuple[int, int]]
) -> list[tuple[int, int, int]]:
    adjacent_numbers = set()

    for index in indicies:
        i, j = index
        while j >= 0 and j < len(data[i]) and data[i][j].isdigit():
            j -= 1
        j += 1

        number, start = "", j
        while data[i][j].isdigit():
            number += data[i][j]
            j += 1

        adjacent_numbers.add((start, j, int(number)))

    return list(adjacent_numbers)


def get_adjacent_digit_indicies(
    data: list[str], x: int, y: int
) -> list[tuple[int, int]]:
    indicies = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if data[x + i][y + j].isdigit():
                indicies.append((x + i, y + j))

    return indicies


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.readlines()

    numbers = []

    for i, line in enumerate(data):
        for j, character in enumerate(line.strip()):
            if character == "*":
                adjacent_numbers = get_adjacent_numbers(
                    data, get_adjacent_digit_indicies(data, i, j)
                )
                if len(adjacent_numbers) == 2:
                    numbers.append(adjacent_numbers[0][-1] * adjacent_numbers[1][-1])

    print(sum(numbers))
