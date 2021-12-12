from collections import Counter
from itertools import combinations
from difflib import SequenceMatcher

with open('01.txt', 'r') as f:
    serials = f.readlines()
double = 0
triple = 0
for serial in serials:
    d = Counter(serial)
    double += 1 if 2 in d.values() else 0
    triple += 1 if 3 in d.values() else 0

print('Part 1:', double * triple)


with open('01.txt', 'r') as f:
    serials = (a.strip() for a in f.readlines())

data = combinations(serials, 2)
match_ratio = 0.96
matched_item = ()
for item in data:
    match = SequenceMatcher(a=item[0], b=item[1])
    if match.ratio() > match_ratio:
        matched_item = item

print('Part 2:', ''.join([x for x, y in zip(*matched_item) if x == y]))
