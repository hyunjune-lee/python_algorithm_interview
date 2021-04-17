def find_max_range(nums):
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    left_max = find_max_range(nums[:mid])
    right_max = find_max_range(nums[mid:])

    left = mid_to_left_max = 0
    for l in range(mid - 1, -1, -1):
        left += nums[l]
        mid_to_left_max = max(abs(left), mid_to_left_max)

    right = mid_to_right_max = 0
    for r in range(mid + 1, len(nums)):
        right += nums[r]
        mid_to_right_max = max(abs(right), mid_to_right_max)
    print("nums", nums, mid)
    print(left_max, right_max)
    print(mid_to_left_max, nums[mid], mid_to_right_max)
    print(max(left_max, right_max), abs(mid_to_left_max + nums[mid] + mid_to_right_max))
    mid_sum = mid_sum_max = 0
    for num in (mid_to_left_max, nums[mid], mid_to_right_max):
        mid_sum += num
        mid_sum_max = max(abs(mid_sum), mid_sum_max)
    print("mid sum", mid_sum_max)
    # mid_sum = left_max + nums[mid] + right_max
    return max(max(left_max, right_max), mid_sum_max)


T = int(input())
for _ in range(T):
    N = map(int, input().split())
    nums = list(map(int, input().split()))
    print(abs(find_max_range(nums)))
