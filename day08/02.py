with open('01.txt', 'r') as f:
    data_in = list(map(int, f.read().strip().split()))

meta_data = []
depth = 0
node_list = []
meta_list = []


def parse(data):
    total = 0
    nodes, meta = data[:2]
    data = data[2:]
    ret_nodes = []
    for _ in range(nodes):
        ret_node, data = parse(data)
        ret_nodes.append(ret_node)

    if nodes == 0:
        total += sum(data[:meta])
    else:
        for m in data[:meta]:
            try:
                total += ret_nodes[m-1]
            except IndexError:
                continue
    data = data[meta:]
    return total, data


print('Part 2:', parse(data_in)[0])
