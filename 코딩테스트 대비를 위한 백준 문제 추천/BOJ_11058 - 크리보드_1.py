# [0. 날짜]
# 2021.07.23(금요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 1 23 45678
# I AC VVV
# I IA CVV
# I II ACV
# i 7 이후에는
# VVV
# ?ACVV V => i는 -5 에서 3번 곱한거 근데 각 A + 3A = 4A 이므로 4곱한거라 생각
# ??ACV V => i는 -4 에서 2번 곱한거
# ???AC V => i는 -3 에서 1번 곱한거
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution():
    # dp[n]이 n 번 눌렀을때의 A의 최댓값
    dp = [0 for _ in range(101)]
    for i in range(7):
        dp[i] = i
    for i in range(7, n + 1):
        for j in range(2, 5):
            dp[i] = max(dp[i], dp[i - j - 1] * j)
    return dp[n]


n = int(input())
print(solution())
