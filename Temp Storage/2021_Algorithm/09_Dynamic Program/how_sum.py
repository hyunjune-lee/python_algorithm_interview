# if res => if res is not None: 이렇게 해서 고침..

## if 조건 분할 전 1846ms
def how_sum(m, nums):
    table = [None for _ in range(m + 1)]
    table[0] = []
    for i in range(m):
        if table[i] != None:
            for x in nums:
                if i + x <= m and table[i + x] == None:
                    table[i + x] = table[i] + [x]
                    if i + x == m:
                        return table[m]
    return table[m]


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    nums = list(map(int, input().split()))
    res = how_sum(m, nums)

    if res is not None:
        print(len(res), " ".join(map(str, res)))
    else:
        print(-1)


## if 조건 분할 후 2439ms 아마 뒤에 붙은  table[i + x] == None조건 때문에 오히려 시간이 늘은듯
# def how_sum(m, nums):
#     table = [None for _ in range(m + 1)]
#     table[0] = []
#     for i in range(m):
#         if table[i] != None:
#             for x in nums:
#                 if i + x < m and table[i + x] == None:
#                     table[i + x] = table[i] + [x]
#                 elif i + x == m:
#                     return table[i] + [x]
#     return table[m]


# t = int(input())
# for _ in range(t):
#     m, n = map(int, input().split())
#     nums = list(map(int, input().split()))
#     res = how_sum(m, nums)

#     if res is not None:
#         print(len(res), " ".join(map(str, res)))
#     else:
#         print(-1)
