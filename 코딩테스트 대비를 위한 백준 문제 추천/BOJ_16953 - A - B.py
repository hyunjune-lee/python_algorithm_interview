# [0. 날짜]
# 2021.07.20(화요일)
# 문제 유형: bfs
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 최솟값이기 때문에 bfs로 접근
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from collections import deque


def bfs(start_num):
    queue = deque([(start_num, 1)])
    while queue:
        cur_num, cal_count = queue.popleft()
        if cur_num == B:
            return cal_count
        elif cur_num > B:
            continue
        queue.append((cur_num * 2, cal_count + 1))
        queue.append((cur_num * 10 + 1, cal_count + 1))
    return -1


A, B = map(int, input().split())
print(bfs(A))
