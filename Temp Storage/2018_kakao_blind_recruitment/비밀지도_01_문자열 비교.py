# 20분
from collections import deque


def solution(n, arr1, arr2):
    res = []
    for i in range(n):
        temp_arr1 = deque([])
        num1 = arr1[i]
        while num1 > 0:
            temp_arr1.appendleft(num1 % 2)
            num1 = num1 // 2
        while len(temp_arr1) < n:
            temp_arr1.appendleft(0)

        temp_arr2 = deque([])
        num2 = arr2[i]
        while num2 > 0:
            temp_arr2.appendleft(num2 % 2)
            num2 = num2 // 2
        while len(temp_arr2) < n:
            temp_arr2.appendleft(0)

        res_row = ""
        for j in range(n):
            if temp_arr1[j] or temp_arr2[j]:
                res_row += "#"
            else:
                res_row += " "
        res.append(res_row)
    return res


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
