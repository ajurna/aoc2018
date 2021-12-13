'419 players; last marble is worth 72164 points'
from collections import defaultdict
from blist import blist
player_count = 452
last_marble = 7078400


scores = defaultdict(int)
circle = blist([0])
current_marble = 0
cur_idx = 0
for marble in range(1, last_marble+1):
    cur_idx = cur_idx + 2
    if cur_idx > len(circle):
        cur_idx = cur_idx - len(circle)
    if marble % 23 == 0:
        cur_idx -= 9
        if cur_idx < 0:
            cur_idx += len(circle)
        temp_marble = circle[cur_idx]
        scores[marble % player_count] += marble + temp_marble
        del(circle[cur_idx])
        current_marble = circle[cur_idx]
    else:
        current_marble = marble
        circle.insert(cur_idx, marble)


print(max(scores.values()))


