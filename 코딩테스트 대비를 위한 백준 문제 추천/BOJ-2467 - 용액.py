# [0. 날짜]
# 2021.07.21(수요일)
# 문제 유형: 투포인터
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 투포인터의 어느방향을 진행시킬지에 대한
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution():
    l, r = 0, N - 1
    min_gap = liquid[l] + liquid[r]
    res = [liquid[l], liquid[r]]
    while l < r:
        gap = liquid[l] + liquid[r]
        if abs(gap) < abs(min_gap):
            min_gap = gap
            res = [liquid[l], liquid[r]]
            if gap == 0:
                break
        if gap < 0:
            l += 1
        else:
            r -= 1

    return res


N = int(input())
liquid = list(map(int, input().split()))


print(" ".join(map(str, solution())))
