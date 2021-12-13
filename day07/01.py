from dataclasses import dataclass, field
from string import ascii_uppercase


@dataclass
class Node:
    step: str
    required: list = field(default_factory=list)
    completed: bool = field(init=False, default=False)

    def __hash__(self):
        return hash(self.step)


class Graph:
    def __init__(self):
        self.nodes = {}
        self.completed_nodes = []
        self.nodes_to_complete = []

    def parse(self, r_line: str):
        r_line = r_line.split()
        pre_node_l = r_line[1]
        post_node_l = r_line[7]
        if post_node_l in self.nodes:
            post_node = self.nodes[post_node_l]
        else:
            self.nodes[post_node_l] = Node(post_node_l)
            post_node = self.nodes[post_node_l]
        if pre_node_l in self.nodes:
            pre_node = self.nodes[pre_node_l]
        else:
            self.nodes[pre_node_l] = Node(pre_node_l)
            pre_node = self.nodes[pre_node_l]
        post_node.required.append(pre_node)

    def compute_nodes(self):
        for le in ascii_uppercase:
            if le in self.nodes:
                self.nodes_to_complete.append(le)


graph = Graph()
with open('01.txt', 'r') as f:
    for line in f.readlines():
        graph.parse(line)
graph.compute_nodes()

while graph.nodes_to_complete:
    for node_letter in graph.nodes_to_complete:
        node = graph.nodes[node_letter]
        steps_finished = all([graph.nodes[x.step].completed for x in node.required])
        if steps_finished:
            graph.completed_nodes.append(node_letter)
            graph.nodes_to_complete.remove(node_letter)
            node.completed = True
            break

print('Part 1:', "".join(graph.completed_nodes))
