def get_mapped_value(value: int, maps: list[str]) -> int:
    for destination, source, length in maps:
        if source <= value < source + length:
            return destination + (value - source)

    return value


def get_minimum_distance(seeds: list[str], m: dict[str, dict[int, int]]) -> int:
    distances = []

    for seed in seeds:
        s2s = get_mapped_value(int(seed), m["seed-to-soil"])
        s2f = get_mapped_value(s2s, m["soil-to-fertilizer"])
        f2w = get_mapped_value(s2f, m["fertilizer-to-water"])
        w2l = get_mapped_value(f2w, m["water-to-light"])
        l2t = get_mapped_value(w2l, m["light-to-temperature"])
        t2h = get_mapped_value(l2t, m["temperature-to-humidity"])
        h2l = get_mapped_value(t2h, m["humidity-to-location"])
        distances.append(h2l)

    return min(distances)


if __name__ == "__main__":
    with open("input.txt") as file:
        data = file.read()

    sections = data.split("\n\n")

    seeds = sections[0].strip().split(":")[1].split()
    conversion_maps = {}

    for section in sections[1:]:
        name, data = section.split(":")
        conversion_maps[name.split()[0]] = [
            tuple(map(int, line.split())) for line in data.strip().split("\n")
        ]

    minimum_distance = get_minimum_distance(seeds, conversion_maps)

    print(minimum_distance)
