# [0. 날짜]
# 2021.07.20(화요일)
# 문제 유형: 위상정렬, DP
# 걸린 시간: 20분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 주어진 화살표를 반대로 해서 끝에서부터 더해서 delay를 구해본다.
# 1. leaf node이면 자신의 건설시간만 return
# 2. 중간이면 자신이 가진 leaf node중에서 최대하고 자신의 건설시간을 더한 값을 return
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
#     if total_build_time_list[building_idx] != -1:
#       return total_build_time_list[building_idx]
# visited 개념을 안 넣어줘서 시간초과
# visited는 늘 생각해야겠다..
from collections import defaultdict
import sys

limit_number = 15000
sys.setrecursionlimit(limit_number)


def dfs(building_idx):
    if total_build_time_list[building_idx] != -1:
        return total_build_time_list[building_idx]
    build_time = build_time_list[building_idx]
    # 1. leaf node이면 자신의 건설시간만 return
    if not graph[building_idx]:
        total_build_time_list[building_idx] = build_time
        return build_time
    # 2. 중간이면 자신이 가진 leaf node중에서 최대하고
    # 자신의 건설시간을 더한 값을 return
    max_build_delay = 0
    for need_building_idx in graph[building_idx]:
        max_build_delay = max(max_build_delay, dfs(need_building_idx))

    total_build_time_list[building_idx] = build_time + max_build_delay
    return build_time + max_build_delay


T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    build_time_list = [0] + list(map(int, input().split()))
    total_build_time_list = [-1 for _ in range(N + 1)]

    graph = defaultdict(list)
    for _ in range(K):
        u, v = map(int, input().split())
        graph[v].append(u)
    W = int(input())

    print(dfs(W))
