# 20분
from collections import deque


def solution(n, arr1, arr2):
    maps = []
    for i in range(n):
        maps.append(bin(arr1[i] | arr2[i])[2:].zfill(n).replace("1", "#").replace("0", " "))
    return maps


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
