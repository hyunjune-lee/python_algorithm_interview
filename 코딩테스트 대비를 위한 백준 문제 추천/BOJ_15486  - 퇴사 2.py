# [0. 날짜]
# 2021.08.01(일요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 1일부터 끝까지 진행하면서
# 1. 오늘의 금액이 전날의 금액이 큰지, 아니면 전에 일하다 오늘 마친후의 금액이 큰지 확인한다.
# 2. 오늘 일했을 때의 다음날의 금액을 갱신해놓는다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution():
    for i in range(1, N + 1):
        take_time, amount = counseling_list[i - 1]
        # 오늘의 금액이 전날의 금액이 큰지, 아니면 전에 일하다 오늘 마친후의 금액이 큰지?
        dp_amount[i] = max(dp_amount[i - 1], dp_amount[i])
        # 오늘 일했을 때의 다음 날의 금액
        if i + take_time < N + 2:
            dp_amount[i + take_time] = max(dp_amount[i + take_time], dp_amount[i] + amount)
    dp_amount[N + 1] = max(dp_amount[N], dp_amount[N + 1])
    return dp_amount[N + 1]


N = int(input())
counseling_list = []
for _ in range(N):
    counseling_list.append(list(map(int, input().split())))

dp_amount = [0 for _ in range(N + 2)]


print(solution())
