# [0. 날짜]
# 2021.07.13(화요일)
# 문제 유형: 수학, 구현
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def easy_problem(a, b):
    nums = [0 for _ in range(b + 1)]
    i = 0
    for delta_limit in range(1, 200):
        for _ in range(0, delta_limit):
            if i == b + 1:
                return sum(nums[a - 1 : b])
            nums[i] = delta_limit
            i += 1

    return sum(nums[a - 1 : b])


print(easy_problem(*map(int, input().split())))
