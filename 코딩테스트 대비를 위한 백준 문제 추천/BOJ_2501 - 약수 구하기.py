# [0. 날짜]
# 2021.07.13(화요일)
# 문제 유형: 수학
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 주어진 숫자를 1~N까지의 숫자로 나눠서 나머지 0이면 그 숫자는 약수이다.
# 약수가 나올때마다 k_count를 세서 k번째가 되면 해당 숫자를 반환해줍니다.
# 만약 k번째 약수가 없다면 0을 반환해줍니다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def find_kth_divisor(N, K):
    k_count = 0
    for num in range(1, N + 1):
        if N % num == 0:
            k_count += 1
            if k_count == K:
                return num

    return 0


N, K = list(map(int, input().split()))
print(find_kth_divisor(N, K))
