# [0. 날짜]
# 2021.07.19(월요일)
# 문제 유형: DP
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 이 문제 같은 경우에는 같은 개수의 동전을 사용했으면 동전의 사용순서에 상관없이 같은 것으로 취급하기 때문에
# 동전의 사용 순서를 강제해야된다..
# 하지만 나는 바깥쪽에서 동전 사용을 강제할 생각을 못하고ㅠ
# 안쪽에서 계속 인덱스를 저장해서 동전 사용 순서를 강제하려고 했다..
# 이것도 사소하지만 중요한 테크닉인것 같다.


def solution():
    for coin in coin_list:
        for i in range(k):
            if sum_count_list[i] != 0:
                if (coin_sum := coin + i) <= k:
                    sum_count_list[coin_sum] += sum_count_list[i]
    return sum_count_list[k]


n, k = map(int, input().split())
sum_count_list = [0 for _ in range(k + 1)]
sum_count_list[0] = 1
coin_list = []
for _ in range(n):
    coin_list.append(int(input()))
print(solution())
