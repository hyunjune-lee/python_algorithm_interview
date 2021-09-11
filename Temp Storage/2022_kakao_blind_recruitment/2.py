# [0. 날짜]
# 2021.09.11(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 왜 케이스 1에서 시간초과가 뜨지?
# 소수쪽에서 높은 값이 나와서 그랬네
# 7
# 7 / 2 .. 1
# 3 / 2 .. 1
# 1 / 2 .. 1
# 0

import math


def is_prime(num):
    if num <= 1:
        return False
    for div in range(2, int(math.sqrt(num) + 1)):
        if num % div == 0:
            return False
    return True


def solution(n, k):
    # 진수 변환
    r = 0
    res_str = ""
    while n > 0:
        r = n % k
        res_str += str(r)
        n = n // k
    res_str = res_str[::-1]
    # print(res_str)
    # print(res_str.split("0"))
    res = 0

    for check_num_str in res_str.split("0"):
        if check_num_str and len(check_num_str) > 0 and is_prime(int(check_num_str)):
            res += 1

    return res


# print(solution(1, 3))

print(solution(437674, 3))
print(solution(110011, 10))
for i in range(3, 11):
    print(solution(1, i))
for i in range(3, 11):
    print(solution(1000000, i))
