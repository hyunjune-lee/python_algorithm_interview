import math


def solution(pair):
    # 예외 처리
    if len(pair) < 2:
        return format(0, ".2f")

    px = sorted(pair)
    py = sorted(pair, key=lambda x: x[1])
    answer = closest_pair(px, py)
    return format(answer, ".2f")


def closest_pair(px, py):
    if len(px) <= 3:
        return brute_force(px)

    mid = len(px) // 2
    pxL = px[:mid]
    pyL = [p for p in py if p[0] < px[mid][0]]
    pxR = px[mid:]
    pyR = [p for p in py if p[0] >= px[mid][0]]

    delta = min(closest_pair(pxL, pyL), closest_pair(pxR, pyR))
    return closest_split_pair(px, py, delta)


def get_distance(p1, p2):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))


def brute_force(px):
    min_dist = 100000
    for i in range(len(px) - 1):
        for j in range(i + 1, len(px)):
            min_dist = min(min_dist, get_distance(px[i], px[j]))
    return min_dist


def closest_split_pair(px, py, delta):
    mid = len(px) // 2
    median_X = px[mid][0]

    candidates = []
    for p in py:
        if median_X - delta < p[0] and p[0] < median_X + delta:
            candidates.append(p)

    # 후보자 비교
    for i in range(len(candidates) - 1):
        # for j in range(i + 1, min(i + 8, len(candidates))):
        count = 0
        for j in range(i + 1, len(candidates)):
            dist = get_distance(candidates[i], candidates[j])
            delta = min(delta, dist)
            count += 1
            if count == 7:
                break
    return delta


# 입력 및 실행
for _ in range(int(input())):
    pair_num = int(input())
    arr = list(map(int, input().split()))
    pairs = []
    for i in range(0, pair_num, 2):
        py = arr[i]
        px = arr[i + 1]
        pairs.append((px, py))
    print(solution(pairs))

pair = [(-5, 0), (-3, 4), (2, 1), (3, 4), (-1, 1), (8, 8), (1, 7)]  # 답은 3
# pair = [(1, 0), (2, 0), (5, 0)]
print(solution(pair))
# # 1
# 7
# -5 0 -3 4 2 1 3 4 -1 1 8 8 1 7
# pair = [(1, 0), (2, 0), (3, 0), (4, 0)]
# print(solution(pair))
