# [0. 날짜]
# 2021.07.13(화요일)
# 문제 유형: 구현, 정렬
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 9C2
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
#


def find_3th_max_num(nums):
    return sorted(nums, reverse=True)[2]


for _ in range(int(input())):
    print(find_3th_max_num(map(int, input().split())))
