# [0. 날짜]
# 2021.08.01(일요일)
# 문제 유형: dp
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 1를 먼저 쭉 더하고, 2 쭉 더하고, 3쭉 더하는 식
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

# 188ms
def solution(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1

    for add_num in [1, 2, 3]:
        for x in range(add_num, n + 1):
            dp[x] += dp[x - add_num]
    return dp[n]


T = int(input())
for _ in range(T):
    n = int(input())
    print(solution(n))
