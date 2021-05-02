from typing import List


count_inv = 0


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])
    l = h = 0
    merged_arr = []
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            global count_inv
            count_inv += len(low_arr) - l
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    count_inv = 0
    merge_sort(nums)
    print(count_inv)
