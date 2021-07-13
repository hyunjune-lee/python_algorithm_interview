# [0. 날짜]
# 2021.07.13(화요일)
# 문제 유형: 수학, 유클리드 호제법
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 9C2
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
#

from collections import defaultdict


def get_divsiors(num):
    divsiors = defaultdict(int)
    while num != 1:
        for divisor in range(2, num + 1):
            if num % divisor == 0:
                num //= divisor
                divsiors[divisor] += 1
                break
    return divsiors


# [최대공배수와 두 수의 곱에서 계산.ver]
def find_GCD_n_LCM(a, b):
    a_divsiors = get_divsiors(a)
    b_divsiors = get_divsiors(b)
    GCD = 1
    for num in a_divsiors.keys():
        if b_divsiors[num] > 0:
            GCD *= num ** min(a_divsiors[num], b_divsiors[num])
    print(GCD)
    print(LCM := a * b // GCD)


find_GCD_n_LCM(*map(int, input().split()))


# [모두 약수에서 계산.ver]
# def find_GCD_n_LCM(a, b):
#     a_divsiors = get_divsiors(a)
#     b_divsiors = get_divsiors(b)
#     GCD = 1
#     for num in a_divsiors.keys():
#         if b_divsiors[num] > 0:
#             GCD *= num ** min(a_divsiors[num], b_divsiors[num])
#     print(GCD)
#     nums = list(set(list(a_divsiors.keys()) + list(b_divsiors.keys())))
#     LCM = 1
#     for num in nums:
#         LCM *= num ** max(a_divsiors[num], b_divsiors[num])
#     print(LCM)
