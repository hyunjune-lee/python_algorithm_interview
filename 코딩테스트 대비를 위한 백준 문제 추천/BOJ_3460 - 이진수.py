# [0. 날짜]
# 2021.07.13(화요일)
# 문제 유형: 수학
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 이진수로 변환하면서 1나올때마다 프린트를 해준다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

# [나눗셈.ver]
# def find_one_bit(num):
#     i = 0
#     while num != 0:
#         if num % 2 == 1:
#             print(i, end=" ")
#         num //= 2
#         i += 1
#     return None

# ====================

# [bin 사용.ver]
def find_one_bit(reverse_bin):
    for i, bit in enumerate(reverse_bin):
        if bit == "1":
            print(i, end=" ")
    return None


for _ in range(T := int(input())):
    find_one_bit(bin(int(input()))[::-1])
