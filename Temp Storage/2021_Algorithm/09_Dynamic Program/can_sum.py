# 배열 사용시 1529ms
def can_sum(m, nums):
    table = [False for _ in range(m + 1)]
    table[0] = True
    for i in range(m):
        if table[i]:
            for num in nums:
                if i + num < m:
                    table[i + num] = True
                elif i + num == m:
                    return True
    return table[m]


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    nums = list(map(int, input().split()))
    print(str(can_sum(m, nums)).lower())


# 배열 사용 + if 조건 분할 안 했을때 2147ms
def can_sum(m, nums):
    table = [False for _ in range(m + 1)]
    table[0] = True
    for i in range(m):
        if table[i]:
            for num in nums:
                if i + num <= m:
                    table[i + num] = True
                    if i + num == m:
                        return True
    return table[m]


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    nums = list(map(int, input().split()))
    print(str(can_sum(m, nums)).lower())


# dict 사용시 1787ms
# from collections import defaultdict


# def can_sum(m, nums):
#     table = defaultdict(bool)
#     table[0] = True
#     for i in range(m - 1):
#         if table[i]:
#             for num in nums:
#                 if i + num < m:
#                     table[i + num] = True
#                 elif i + num == m:
#                     return True
#     return table[m]
