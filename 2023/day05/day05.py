def get_mapped_value(value: int, maps: list[str]) -> int:
    for line in maps:
        destination, source, length = line
        if source <= value < source + length:
            return destination + (value - source)

    return value


def get_minimum_distance(seeds: list[str], m: dict[str, dict[int, int]]) -> int:
    distances = []

    for seed in seeds:
        distances.append(
            get_mapped_value(
                get_mapped_value(
                    get_mapped_value(
                        get_mapped_value(
                            get_mapped_value(
                                get_mapped_value(int(seed), m["seed-to-soil"]),
                                m["soil-to-fertilizer"]
                            ),
                            m["fertilizer-to-water"]
                        ),
                        m["water-to-light"]
                    ),
                    m["light-to-temperature"]
                ),
                m["humidity-to-location"]
            )
        )

    return min(distances)


if __name__ == "__main__":
    with open("input1.txt") as file:
        data = file.read()

    sections = data.split("\n\n")

    seeds = sections[0].strip().split(":")[1].split()
    conversion_maps = {}

    for section in sections[1:]:
        name, data = section.split(":")
        conversion_maps[name.split()[0]] = [tuple(map(int, line.split())) for line in data.strip().split("\n")]
        print(f"{name} done converting")

    minimum_distance = get_minimum_distance(seeds, conversion_maps)

    print(minimum_distance)
