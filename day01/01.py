total = 0
with open('01.txt', 'r') as f:
    for n in f.readlines():
        total += int(n)

print('Part 1:', total)

visited_freq = set()
freq = 0
visited_freq.add(freq)


def items(changes):
    while True:
        for i in changes:
            yield i


with open('01.txt', 'r') as f:
    freq_cycle = [int(n) for n in f.readlines()]
next_change = items(freq_cycle)

while True:
    freq += next(next_change)
    if freq in visited_freq:
        break
    visited_freq.add(freq)

print('Part 2:', freq)
