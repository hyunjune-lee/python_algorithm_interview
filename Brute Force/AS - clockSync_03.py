INF = 9999
SWITCHES_COUNT = 10

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


def push(clocks, switch_idx):
    for switch in switches_list[switch_idx]:
        if clocks[switch] == 12:
            clocks[switch] = 3
        else:
            clocks[switch] += 3

    return clocks


def solve(clocks, switch_idx):
    if switch_idx == SWITCHES_COUNT:
        return 0 if isAll12(clocks) else INF
    ret = INF
    for i in range(4):
        ret = min(ret, i + solve(clocks, switch_idx + 1))
        clocks = push(clocks, switch_idx)

    return ret


C = int(input())

for _ in range(C):
    clocks = list(map(int, input().split()))
    print(solve(clocks, 0))
