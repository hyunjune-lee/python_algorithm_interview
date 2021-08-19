# [0. 날짜]
# 2021.08.16(월요일)
# 문제 유형: dp
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 누적되면서 기억할 수 있는 사항에 대해 생각해보기
# 팰린드롬에서는 현재 양끝의 숫자가 같고 안쪽의 문자열이 팰린드롬이면 팰린드롬이다.
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 워낙 입력받는게 많아서sys.stdin.readline().rstrip()을 적용해줘야 했다.
import sys

N = int(input())
nums = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
memo = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]


def sol(s, e):
    if memo[s][e] >= 0:
        return memo[s][e]
    if s >= e:
        return 1

    if nums[s] == nums[e]:
        memo[s][e] = sol(s + 1, e - 1)
    else:
        memo[s][e] = 0
    return memo[s][e]


for _ in range(M):
    print(sol(*map(int, sys.stdin.readline().rstrip().split())))
