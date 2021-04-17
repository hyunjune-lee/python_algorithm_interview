switches_list = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13],
]


def isAll12(clocks):
    for i in clocks:
        if i != 12:
            return False
    return True


switch_count = [0 for _ in range(len(switches_list))]
path = [-1 for _ in range(3 * len(switches_list))]


def run(level, idx, clocks):
    print(level, clocks)
    print(path)
    if level == 3 * len(switches_list):
        return

    if isAll12(clocks):
        print(level)
        return level
    for switches_idx in range(idx, len(switches_list)):
        if switch_count[switches_idx] < 3:
            switch_count[switches_idx] += 1
            switches = switches_list[switches_idx]
            for switch in switches:
                if clocks[switch] == 12:
                    clocks[switch] = 3
                else:
                    clocks[switch] += 3
            path[level] = switches_idx
            run(level + 1, switches_idx, clocks)
            path[level] = -1
            switch_count[switches_idx] -= 1
            for switch in switches:
                if clocks[switch] == 3:
                    clocks[switch] = 12
                else:
                    clocks[switch] -= 3
    return


C = int(input())

for _ in range(C):
    clocks = list(map(int, input().split()))
    # print(run(0, -1, clocks))
    print(run(0, 0, clocks))

    isAll12(clocks)
