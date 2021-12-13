from dataclasses import dataclass, field


@dataclass
class Point:
    x: int
    y: int
    infinte: bool = False
    score: int = 0

    def __hash__(self):
        return hash(f'{self.x}, {self.y}')

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


with open('01.txt', 'r') as f:
    points = [Point(*map(int, x.split(', '))) for x in f.readlines()]

print(points)

max_x = max(x.x for x in points)
max_y = max(x.y for x in points)


for y in range(max_y+1):
    for x in range(max_x+1):
        cur_p = Point(x, y)
        scores = [(p.distance(cur_p), p) for p in points]
        scores.sort(key=lambda x: x[0], reverse=True)
        last_1 = scores.pop()
        last_2 = scores.pop()
        if last_1[0] != last_2[0]:
            last_1[1].score += 1
            if cur_p.x == 0 or cur_p.y == 0 or cur_p.x == max_x or cur_p.y == max_y:
                last_1[1].infinte = True

print('Part 1:', sorted([p for p in points if not p.infinte], key=lambda x: x.score)[-1].score)
