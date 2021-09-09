# [0. 날짜]
# 2021.08.25(수요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 첫번째 되는 소수는 2,3,5,7이다.
# 두번째 이후에 되는 후보는 1,3,5,7,9이다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# dfs, 두번째부터 소수체크하면서 가지치기 하기
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from math import sqrt


def prime_check(prime_num):
    check_num = 2
    while check_num <= sqrt(prime_num):
        if prime_num % check_num == 0:
            return False
        check_num += 1
    return True


def solution(N):
    def dfs(n, prime_num_list):
        if n == N:
            print("".join(map(str, prime_num_list)))
            return
        candidates = [1, 3, 5, 7, 9]
        if n == 0:
            candidates = [2, 3, 5, 7]
        for candidate in candidates:
            prime_num_list.append(candidate)
            if prime_check(int("".join(map(str, prime_num_list)))):
                dfs(n + 1, prime_num_list)
            prime_num_list.pop()

    dfs(0, [])


solution(int(input()))
