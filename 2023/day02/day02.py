from functools import reduce
import operator


def get_draws(line: str) -> list[list[str]]:
    draws = []

    for draw in line.split(": ")[1].split("; "):
        draws.append([count.replace("\n", "") for count in draw.split(", ")])

    return draws


def get_maximum_color_counts(draws: list[list[str]]) -> list[int]:
    maximum_values = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for draw in draws:
        for count in draw:
            value, color = count.split()
            if int(value) > maximum_values[color]:
                maximum_values[color] = int(value)

    return maximum_values.values()


if __name__ == "__main__":

    with open("input.txt") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        total += reduce(operator.mul, get_maximum_color_counts(get_draws(line)), 1)

    print(total)
