from parse import compile
parse_guard = compile('[{y}-{M}-{d} {h}:{m}] Guard #{guard} begins shift')
parse_sleep = compile('[{date} {h}:{m}] {}')

with open('01.txt', 'r') as f:
    data = sorted((map(str.strip, f.readlines())))
master = dict()
guard = 0
while data:
    line = data.pop(0)
    if 'Guard' in line:
        parsed = parse_guard.parse(line)
        guard = parsed['guard']
        if guard not in master:
            master[guard] = dict()
    elif 'falls' in line:
        parsed = parse_sleep.parse(line)

        date = parsed['date']
        sleep_time = line.split()[1][3:5]

        wake = data.pop(0)
        wake_parsed = parse_sleep.parse(wake)

        wake_time = wake_parsed['m']

        if date not in master[guard]:
            master[guard][date] = [0 for _ in range(60)]
        for x in range(int(sleep_time), int(wake_time)):
            master[guard][date][x] = 1

minutes_slept = []
for guard, dates in master.items():
    minutes = 0
    for date in dates:
        minutes += sum(dates[date])
    minutes_slept.append((minutes, guard))
minutes_slept.sort(reverse=True)
print(minutes_slept)
minutes, guard = minutes_slept.pop(0)
minutes_per_minute = sorted([(sum(v), k) for k, v in enumerate(zip(*master[guard].values()))], reverse=True)

total_mins, minute_number = minutes_per_minute.pop(0)

print('Part 1: ', int(guard)*minute_number)

new_data = []
for guard in master:
    try:
        top_minutes = sorted([(sum(v), k) for k, v in enumerate(zip(*master[guard].values()))], reverse=True)[0]
        new_data.append((top_minutes[0], top_minutes[1], guard))
    except IndexError:
        continue
new_data.sort()
answer = new_data.pop()
print('Part 2: ', int(answer[2])*answer[1])
