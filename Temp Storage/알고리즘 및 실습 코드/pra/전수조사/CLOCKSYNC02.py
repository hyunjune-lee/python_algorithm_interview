linked = [
    [8, [6, 7, 8, 10, 12]],
    [10, [4, 10, 14, 15]],
    [11, [3, 7, 9, 11]],
    [9, [3, 4, 5, 9, 13]],
    [6, [0, 4, 5, 6, 7]],
    [7, [4, 5, 7, 14, 15]],
    [4, [1, 2, 3, 4, 5]],
    [1, [0, 1, 2]],
    [0, [0, 2, 14, 15]],
    [3, [3, 14, 15]],
]

for _ in range(int(input())):
    clocks = list(map(int, input().split()))

    ret = 0
    for clock, idx in linked:
        # print(f'clock {clock} idx {idx}')
        cnt = ((12 - clocks[clock]) % 12) / 3
        ret += cnt
        for i in idx:
            clocks[i] = (clocks[i] + 3 * cnt) % 12

    print(-1 if any(clocks) else int(ret))
