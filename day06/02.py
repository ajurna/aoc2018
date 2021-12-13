from dataclasses import dataclass, field


@dataclass
class Point:
    x: int
    y: int
    id: str = field(init=False, default='--')

    def __hash__(self):
        return hash(f'{self.x}, {self.y}')

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


def draw_grid(d_grid):
    for d_row in d_grid:
        print(' '.join(map(str, d_row)))


with open('01.txt', 'r') as f:
    data_orig = [Point(*map(int, x.split(', '))) for x in f.readlines()]
    i = 0
    for data in data_orig:
        data.id = str(i).zfill(2)
        i += 1

max_x = max(x.x for x in data_orig)
max_y = max(x.y for x in data_orig)

grid = [['..' for _ in range(max_x)] for _ in range(max_y)]

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        p = Point(x, y)
        grid[y][x] = sum([p.distance(x) for x in data_orig])

total = 0
cell: int
for row in grid:
    for cell in row:
        if cell < 10000:
            total += 1
print('Part 2:', total)
