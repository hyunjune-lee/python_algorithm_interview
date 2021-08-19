# [0. 날짜]
# 2021.07.21(수요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# A는 ..
# B는 자신보다 앞에 있는 A의 개수 만큼 늘린다.
# C는 자신보다 앞에 있는 A의 개수, B의 개수만큼 늘린다.
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 이전까지의 A,B의 개수가 동일하다면 또 할 필요가 없다.
# [IMP] dp의 배열의 차원이 늘어나는 경우를 생각해!! 이번 같은 경우 4차원 배열..
# dfs에 메모이제이션, 그리고 문자를 추가하는 지점을 문자열의 뒤로 한정해서
# 늘어나는 규칙을 좀 더 간단하게 함
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 'A', 'B', 'C'로 이루어져 있다는게.. 무조건 있어야 된다고 생각했음
#


def dfs(i, a, b, pair_count):
    if i == N:
        if pair_count == K:
            return True
        return False
    if cache[i][a][b][pair_count]:
        return False
    cache[i][a][b][pair_count] = True
    for c in ["A", "B", "C"]:
        ans_str[i] = c
        if c == "A":
            res = dfs(i + 1, a + 1, b, pair_count)
        elif c == "B":
            res = dfs(i + 1, a, b + 1, pair_count + a)
        elif c == "C":
            res = dfs(i + 1, a, b, pair_count + a + b)
        if res:
            return True
    return False


# 436은 pair의 최대 크기가 435(= 30 * 29 / 2라서)
N, K = map(int, input().split())
ans_str = [None for _ in range(N)]
cache = [[[[0 for _ in range(436)] for _ in range(31)] for _ in range(31)] for _ in range(31)]
if dfs(0, 0, 0, 0):
    print("".join(ans_str))
else:
    print(-1)
