with open('01.txt', 'r') as f:
    data_input = list(map(int, f.read().strip().split()))

meta_data = []
depth = 0
node_list = []
meta_list = []


def parse(data):
    total = 0
    nodes, meta = data[:2]
    data = data[2:]
    for _ in range(nodes):
        ret_total, data = parse(data)
        total += ret_total

    total += sum(data[:meta])
    data = data[meta:]
    return total, data


print('Part 1:', parse(data_input)[0])
