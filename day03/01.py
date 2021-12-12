import re
from dataclasses import dataclass, field

grid = [[set() for _ in range(1000)] for _ in range(1000)]

claim_re = re.compile(r'^#(?P<id>\d+) @ (?P<x>\d+),(?P<y>\d+): (?P<w>\d+)x(?P<h>\d+)$')


@dataclass
class Claim:
    data: str = field(repr=False)
    id: int = field(init=False)
    x: int = field(init=False)
    x2: int = field(init=False)
    y: int = field(init=False)
    y2: int = field(init=False)
    w: int = field(init=False)
    h: int = field(init=False)

    def __post_init__(self):
        [setattr(self, x, int(y)) for x, y in claim_re.match(self.data.strip()).groupdict().items()]
        self.x2 = self.x + self.w
        self.y2 = self.y + self.h

    def coords(self):
        for x in range(self.x, self.x2):
            for y in range(self.y, self.y2):
                yield x, y


with open('01.txt', 'r') as f:
    claim_list = [Claim(x) for x in f.readlines()]

for claim in claim_list:
    for coord in claim.coords():
        grid[coord[0]][coord[1]].add(claim.id)

count = 0
for row in grid:
    count += len(list(filter(lambda x: len(x) > 1, row)))

print('Part 1:', count)

with open('01.txt', 'r') as f:
    claim_list = [Claim(x) for x in f.readlines()]

for claim in claim_list:
    for coord in claim.coords():
        grid[coord[0]][coord[1]].add(claim.id)

dups = set()

for row in grid:
    for cell in row:
        if len(cell) > 1:
            for item in cell:
                dups.add(item)
claims = set(x.id for x in claim_list)

print('Part 2:', list(claims.difference(dups))[0])
