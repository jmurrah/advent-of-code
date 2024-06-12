def get_numbers(data, indicies):
    numbers = []

    for index in indicies:
        i, j = index
        while data[i][j] != ".":
            j -= 1

        j += 1
        
        number, start = "", j
        # print(data[i][j])
        print(data[i])
        print(i, j)
        while data[i][j].isdigit():
            number += data[i][j]
            j += 1
        
        numbers.append((start, i, int(number.strip())))
    
    return numbers


def get_adjacent_digit_indicies(data, x, y):
    indicies = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            if data[x + i][y + j].isdigit():
                indicies.append((x + i, y + j))

    return indicies


if __name__ == "__main__":
    with open("input1.txt") as file:
        data = file.readlines()

    numbers = []
    for i, line in enumerate(data):
        for j, character in enumerate(line.strip()):
            if not character.isdigit() and character != ".":
                numbers.append(get_numbers(data, get_adjacent_digit_indicies(data, i, j)))

    print(sum([number[-1] for number in set(numbers)]))
    