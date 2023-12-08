
import math

type node_type = dict[str, str]


def parse_node(line: str) -> dict[str, node_type]:
    
    node: node_type = {}
    replacements: list[str] = ['\n', ' =', '(', ',', ')']
    for string in replacements:
        line = line.replace(string, '')

    node["value"], node["L"], node["R"] = line.split(' ')[0:3]

    return {node["value"]: node}


def traverse_instruction(starting_node: node_type) -> tuple[int, node_type]:

    current_node: node_type = starting_node
    steps: int = 0

    while (not current_node["value"].endswith('Z')):
        character: str = input_pattern[steps % len(input_pattern)]
        current_node = nodes[current_node[character]]
        steps += 1

    return steps, current_node


def zzz_traverse() -> int:

    current_node: node_type = nodes["AAA"]
    steps: int = 0
    partial_step: int = 0

    while(current_node["value"] != "ZZZ"):
        partial_step, current_node = traverse_instruction(current_node)
        steps += partial_step

    return steps


def parallel_traverse() -> int:

    starting_nodes: list[node_type] = [nodes[node] for node in nodes if node.endswith('A')]
    steps: list[int] = []
    
    for node in starting_nodes:
        steps.append(traverse_instruction(node)[0])

    return math.lcm(*steps)


if __name__ == "__main__":

    nodes: dict[str, node_type] = {}
    input_pattern: str

    with open("day_8/input.txt", "r") as f:
        input_pattern = f.readline().removesuffix('\n')

        for line in f.readlines()[1:]:
            nodes.update(parse_node(line))

    print("Part 1:", zzz_traverse())
    print("Part 2:", parallel_traverse())