# [0. 날짜]
# 2021.07.19(월요일)
# 문제 유형: 완전 탐색
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 감소하는 수의 수열을 만드는 테크닉..
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
#

from collections import deque


def solution():
    if N < 10:
        return N
    dq = deque([])
    n_count = 9
    for i in range(1, 10):
        dq.append(i)
    while dq:
        num = dq.popleft()
        # print(num)
        limit_num = num % 10
        for add_num in range(limit_num):
            n_count += 1
            next_num = num * 10 + add_num
            if n_count == N:
                return next_num
            dq.append(next_num)
    return -1


N = int(input())
print(solution())
