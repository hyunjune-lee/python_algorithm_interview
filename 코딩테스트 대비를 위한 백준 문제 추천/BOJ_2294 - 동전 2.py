# [0. 날짜]
# 2021.07.19(월요일)
# 문제 유형: DP
# 걸린 시간: 15분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 동전 1에서는 계속 더해주었지만 이문제 같은 경우 갱신해준다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# [문제 대충 읽음 문제] => 불가능한 경우 -1 출력 /
# [테스트 대충] => 동전 1에서는 경우의 수를 의미하므로 sum_count_list[0] = 1 이지만 \
#          이 문제에서는 개수이므로 sum_count_list[0] = 0으로 해줘야 한다.


def solution():
    for coin in coin_list:
        for cost in range(k):
            if sum_count_list != float("inf"):
                if (next_cost := cost + coin) <= k:
                    if sum_count_list[next_cost] > sum_count_list[cost] + 1:
                        sum_count_list[next_cost] = sum_count_list[cost] + 1
                    # print(sum_count_list)
    return sum_count_list[k] if sum_count_list[k] != float("inf") else -1


n, k = map(int, input().split())
sum_count_list = [float("inf") for _ in range(k + 1)]
sum_count_list[0] = 0
coin_set = set()
for _ in range(n):
    coin_set.add(int(input()))
coin_list = list(coin_set)
print(solution())
