# [0. 날짜]
# 2021.07.14(수요일)
# 문제 유형: 브루트포스 알고리즘, 백트래킹
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# / 할때  cal //= arr[i + 1] 로 해서 틀림 => cal = int(cal / arr[i + 1])


def dfs(i, cal, add, sub, mul, div):
    global max_val, min_val
    if i == N:
        max_val = max(cal, max_val)
        min_val = min(min_val, cal)
        return
    if add:
        dfs(i + 1, cal + arr[i], add - 1, sub, mul, div)
    if sub:
        dfs(i + 1, cal - arr[i], add, sub - 1, mul, div)
    if mul:
        dfs(i + 1, cal * arr[i], add, sub, mul - 1, div)
    if div:
        dfs(i + 1, int(cal / arr[i]), add, sub, mul, div - 1)


min_val, max_val = +float("inf"), -float("inf")
N = int(input())
arr = list(map(int, input().split()))
op_count_arr = list(map(int, input().split()))
dfs(1, arr[0], *op_count_arr)
print(max_val)
print(min_val)
