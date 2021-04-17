from random import randrange


def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    nums, mid = partition(nums)
    left = quick_sort(nums[:mid])
    right = quick_sort(nums[mid:])
    return left + right


def partition(nums):
    pivot_idx = randrange(len(nums))
    nums[pivot_idx], nums[0] = nums[0], nums[pivot_idx]
    pivot = nums[0]

    i = 1
    for j in range(1, len(nums)):
        if nums[j] < pivot:
            nums[j], nums[i] = nums[i], nums[j]
            i += 1
    nums[0], nums[i - 1] = nums[i - 1], nums[0]
    return nums, i


# 입력 및 실행
for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    print(" ".join(map(str, quick_sort(nums))))
