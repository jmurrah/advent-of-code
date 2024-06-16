def get_card_win_counts_and_queue(data: list[str]) -> tuple[dict[int, int], list[int]]:
    card_win_counts, queue = {}, []

    for i, line in enumerate(data):
        numbers = line.split(":")[1].split("|")
        card_win_counts[i] = len(set(numbers[0].split()) & set(numbers[1].split()))
        queue.append(i)

    return card_win_counts, queue


def get_total_number_of_cards(card_win_counts: dict[int, int], queue: list[int]):
    total = 0

    while queue:
        total += 1
        i = queue.pop()
        queue.extend(list(range(i + 1, i + card_win_counts[i] + 1)))

    return total


if __name__ == "__main__":
    with open("input1.txt") as file:
        data = file.readlines()

    card_win_counts, queue = get_card_win_counts_and_queue(data)
    total_number_of_cards = get_total_number_of_cards(card_win_counts, queue)
    print(total_number_of_cards)
