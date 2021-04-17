def find_max_range(nums, l, h):
    if h - l == 1 or h <= l:
        return nums[l]
    mid = (l + h) // 2

    mid_to_left_max_sum = 0
    mid_to_left_sum = 0
    mid_to_right_max_sum = 0
    mid_to_right_sum = 0
    for left_idx in range(mid - 1, l - 1, -1):
        mid_to_left_sum += nums[left_idx]
        mid_to_left_max_sum = max(mid_to_left_sum, mid_to_left_max_sum)

    for right_idx in range(mid, h):
        mid_to_right_sum += nums[right_idx]
        mid_to_right_max_sum = max(mid_to_right_sum, mid_to_right_max_sum)

    left_max_sum = find_max_range(nums, l, mid)
    right_max_sum = find_max_range(nums, mid, h)

    return max(max(left_max_sum, right_max_sum), mid_to_left_max_sum + mid_to_right_max_sum)


inv_count = 0
for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    print(find_max_range(nums, 0, len(nums)))
