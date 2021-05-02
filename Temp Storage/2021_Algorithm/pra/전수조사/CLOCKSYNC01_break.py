clock_switch_list = [
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


def check_all_12(clocks):
    if sum(clocks) == 12 * 16:
        return True
    else:
        return False


def bfs_clocky_sync(clocks):
    q = []
    q.append(((0, 0), clocks))
    switch_count = 0
    while (True):
        choice_info, next_clocks = q.pop(0)
        choice, choice_count = choice_info
        if check_all_12(next_clocks):
            return 1
        if choice_count == 3:
            choice_count = 0
            choice += 1
        for clock_switch_idx in range(choice, 10):
            new_clocks = next_clocks[:]
            for connect_clock in clock_switch_list[clock_switch_idx]:
                new_clocks[connect_clock] = (new_clocks[connect_clock] % 12) + 3
                q.append(((clock_switch_idx, choice_count + 1), new_clocks))


# 30번까지 눌렀을때 안되면 답이 없음

T = int(input())
for _ in range(T):
    clocks = list(map(int, input().split()))
    print(bfs_clocky_sync(clocks))
