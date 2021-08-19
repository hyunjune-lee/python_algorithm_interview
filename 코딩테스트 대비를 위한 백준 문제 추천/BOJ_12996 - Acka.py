# [0. 날짜]
# 2021.08.09(월요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 일단 곡의 개수 S 만큼의 배열이 존재하고..
# 각 곡마다 고려해야 되는 것은
# dotorya, kesakiyo, hongjun7이 이 곡을 부를지 말지이다.
# 일단 bfs를 적용해볼까..
# 각 곡마다 a, b, c, ab, ac, bc, abc가 부른 경우로..
# 그리고 n번째 곡에서 a,b,c 상태가 똑같다면 그 뒤에 나오는 케이스도 똑같기 때문에
# 이미 구한 상태라면 넘긴다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# n번째 곡에서 a,b,c 상태가 똑같다면 그 뒤에 나오는 케이스도 똑같기 때문에
# 메모이제이션을 통해 기록하고 이미 구한 상태라면 넘긴다.
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 메모이제이션을 적용하는 테크닉이 부족한다.
# n번째의 상태를 생각해보자
from collections import deque


def sol(n, a, b, c):
    if n == S:
        if a + b + c == 0:
            return 1
        return 0
    if memo[n][a][b][c] >= 0:
        return memo[n][a][b][c]

    memo[n][a][b][c] = 0
    for delta_a, delta_b, delta_c in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]:
        na, nb, nc = a - delta_a, b - delta_b, c - delta_c
        if na < 0 or nb < 0 or nc < 0:
            continue
        memo[n][a][b][c] += sol(n + 1, na, nb, nc)
    memo[n][a][b][c] %= 1000000007
    return memo[n][a][b][c]


S, a, b, c = map(int, input().split())
memo = [[[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

print(sol(0, a, b, c))
