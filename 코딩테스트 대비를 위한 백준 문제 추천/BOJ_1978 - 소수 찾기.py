# [0. 날짜]
# 2021.07.13(화요일)
# 문제 유형: 수학, 소수 판정
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from math import sqrt


def is_prime_number(num):
    if num == 1:
        return False
    for divisor in range(2, int(sqrt(num)) + 1):
        if num % divisor == 0:
            return False
    return True


def counting_prime_number(nums):
    count = 0
    for num in nums:
        if is_prime_number(num):
            count += 1
    return count


N = int(input())
print(counting_prime_number(map(int, input().split())))
