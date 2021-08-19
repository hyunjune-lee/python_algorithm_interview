# [0. 날짜]
# 2021.08.18(수요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 몇번째에 a의 개수, b의 개수, c의 개수,쌍의 개수
# 쌍을 초과하는 케이스는 더 진행하지 않는다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def sol(a, b, c, pair_cnt):
    if memo[a][b][c][pair_cnt]:
        return False
    memo[a][b][c][pair_cnt] = True
    if len(history) > N or pair_cnt > K:
        return False
    elif len(history) == N and pair_cnt == K:
        print("".join(history))
        return True

    history.append("A")
    if sol(a + 1, b, c, pair_cnt):
        return True
    history.pop()
    history.append("B")
    if sol(a, b + 1, c, pair_cnt + a):
        return True
    history.pop()
    history.append("C")
    if sol(a, b, c + 1, pair_cnt + a + b):
        return True
    history.pop()
    return False


history = []
N, K = map(int, input().split())
memo = [[[[False for _ in range(15 * 29 + 1)] for _ in range(32)] for _ in range(32)] for _ in range(32)]


if not sol(0, 0, 0, 0):
    print(-1)
