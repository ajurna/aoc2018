import math
import re
from dataclasses import dataclass, field
from functools import reduce
from typing import List

point_re = re.compile(r'position=<\s*(?P<x>-?\d+),\s*(?P<y>-?\d+)> velocity=<\s*(?P<x_delta>-?\d+),\s*(?P<y_delta>-?\d+)>')


@dataclass
class Point:
    data: str = field(repr=False)
    x: int = field(init=False)
    y: int = field(init=False)
    x_delta: int = field(init=False)
    y_delta: int = field(init=False)

    def __post_init__(self):
        [setattr(self, x, int(y)) for x, y in point_re.match(self.data.strip()).groupdict().items()]

    def move(self):
        self.x += self.x_delta
        self.y += self.y_delta


with open('01.txt', 'r') as f:
    data = [Point(x) for x in f.readlines()]

min_area = float('inf')
best_tick = 0
for iter in range(20000):
    [p.move() for p in data]
    x_data = [p.x for p in data]
    y_data = [p.y for p in data]
    min_x = min(x_data)
    min_y = min(y_data)
    max_x = max(x_data)
    max_y = max(y_data)
    new_area = abs(max_x - min_x) * abs(max_y - min_y)
    if new_area < min_area:
        best_tick = iter+1
        min_area = new_area


with open('01.txt', 'r') as f:
    data = [Point(x) for x in f.readlines()]

[p.move() for p in data for _ in range(best_tick)]
min_x = reduce(lambda x, y: min(x, y), [p.x for p in data])
min_y = reduce(lambda x, y: min(x, y), [p.y for p in data])
max_x = reduce(lambda x, y: max(x, y), [p.x for p in data])
max_y = reduce(lambda x, y: max(x, y), [p.y for p in data])

grid = [[' '] * (max_x - min_x + 1)for _ in range(min_y, max_y+1)]
for p in data:
    grid[p.y - min_y][p.x - min_x] = '#'
print('Part 1:')
for line in grid:
    print(''.join(line))
print('Part 2:', best_tick)
