
def split_by_space() -> list[list[str]]:

    groups: list[list[str]] = [[]]
    index: int = 0

    for line in lines:
        if (line == '\n'):
            index += 1
            groups.append([])
        else:
            groups[index].append(line.removesuffix('\n'))

    return groups


def get_maps() -> None:

    for index in range(len(groups)-1):
        transformations[index] = []
        for str_list in (values.split(' ') for values in groups[index+1][1:]):
            transformations[index].append([int(value) for value in str_list])


def transform_seed(seed: int) -> int:

    for _, transform_list in transformations.items():
        for transform in transform_list:
            right_limit: int = transform[1]+transform[2]
            if seed in range(transform[1], right_limit):
                seed = (seed - transform[1]) + transform[0]
                break

    return seed


if __name__ == "__main__":
    
    lines: list[str]
    seeds: list[int]
    transformations: dict[int, list[list[int]]] = dict()


    with open("day_5/input.txt", "r") as f:
        lines = f.readlines()

    groups: list[list[str]] = split_by_space()
    seeds = [int(value) for value in groups[0][0].split(' ')[1:]]
    get_maps()
    seeds = [transform_seed(seed) for seed in seeds]
    
    print("Part 1:", min(seeds))
