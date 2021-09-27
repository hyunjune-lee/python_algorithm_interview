# [0. 날짜]
# 2021.09.27(월요일)
# 문제 유형: dp
# 걸린 시간: 10분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기] 

N = int(input())
costs = []
for _ in range(N):
    costs.append(list(map(int, input().split())))

min_cost = costs[0][:]
for i in range(1, N):
    next_min_cost = [float('inf'), float('inf'), float('inf')]
    next_min_cost[0] = costs[i][0] + min(min_cost[1], min_cost[2])
    next_min_cost[1] = costs[i][1] + min(min_cost[0], min_cost[2])
    next_min_cost[2] = costs[i][2] + min(min_cost[0], min_cost[1])
    min_cost = next_min_cost

print(min(min_cost))


