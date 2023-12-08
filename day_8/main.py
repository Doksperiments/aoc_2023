
type node_type = dict[str, str]


def parse_node(line: str) -> dict[str, node_type]:
    
    node: node_type = {}
    replacements: list[str] = ['\n', ' =', '(', ',', ')']
    for string in replacements:
        line = line.replace(string, '')

    node["value"], node["L"], node["R"] = line.split(' ')[0:3]

    return {node["value"]: node}


def traverse_instruction():

    current_node: node_type = nodes["AAA"]
    steps: int = 0

    while (current_node["value"] != "ZZZ"):
        character: str = input_pattern[steps % len(input_pattern)]
        current_node = nodes[current_node[character]]
        steps += 1

    return steps


if __name__ == "__main__":

    nodes: dict[str, node_type] = {}
    input_pattern: str

    with open("day_8/input.txt", "r") as f:
        input_pattern = f.readline().removesuffix('\n')

        for line in f.readlines()[1:]:
            nodes.update(parse_node(line))

    print("Part 1:", traverse_instruction())