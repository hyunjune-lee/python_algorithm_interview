def find_max_range(nums):
    if len(nums) == 1:
        return abs(nums[0])

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
    print(mid_to_left_max, mid_to_right_max, left_max, nums[mid], right_max)
    return max(max(mid_to_left_max, mid_to_right_max), left_max + nums[mid] + right_max)


T = int(input())
for _ in range(T):
    N = map(int, input().split())
    nums = list(map(int, input().split()))
    print(find_max_range(nums))
