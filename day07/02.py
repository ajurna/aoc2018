from dataclasses import dataclass, field
from string import ascii_uppercase
from typing import Dict


@dataclass
class Node:
    step: str
    required: list = field(default_factory=list)
    completed: bool = field(init=False, default=False)
    time_left: int = field(init=False, default=0)

    def __post_init__(self):
        self.time_left = ascii_uppercase.index(self.step) + 61

    def __hash__(self):
        return hash(self.step)


class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.completed_nodes = []
        self.nodes_to_complete = []
        self.nodes_in_progress = []

        self.worker_count = 5

    def parse(self, p_line: str):
        p_line = p_line.split()
        pre_node_l = p_line[1]
        post_node_l = p_line[7]
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

    def nodes_ready(self):
        out = []
        for node_letter in graph.nodes_to_complete:
            node = graph.nodes[node_letter]
            if all([graph.nodes[x.step].completed for x in node.required]):
                out.append(node_letter)
        return out

    def tick_workers(self):
        for node_letter in list(self.nodes_in_progress):
            node = self.nodes[node_letter]
            node.time_left -= 1
            if node.time_left == 0:
                self.complete_node(node_letter)

    def complete_node(self, node_letter):
        self.completed_nodes.append(node_letter)
        self.nodes_in_progress.remove(node_letter)
        self.nodes[node_letter].completed = True

    def workers_available(self):
        if len(self.nodes_in_progress) < self.worker_count:
            return True

    def start_next_job(self):
        next_job = self.nodes_ready().pop(0)
        self.nodes_in_progress.append(next_job)
        self.nodes_to_complete.remove(next_job)


graph = Graph()
with open('01.txt', 'r') as f:
    for line in f.readlines():
        graph.parse(line)
graph.compute_nodes()

total_seconds = 0
while graph.nodes_to_complete or graph.nodes_in_progress:
    while graph.workers_available() and graph.nodes_ready():
        graph.start_next_job()
    graph.tick_workers()
    while graph.workers_available() and graph.nodes_ready():
        graph.start_next_job()
    total_seconds += 1
print('Part 1:', total_seconds)
