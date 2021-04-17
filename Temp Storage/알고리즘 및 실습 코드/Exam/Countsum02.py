def count_sum(gap_to_target, idx, nums, start, end):
    if gap_to_target < 0:
        return 0
    elif gap_to_target == 0:
        print(path)
        ret_list.append(path[:])
        return 1
    ret = 0
    while idx < len(nums):
        path.append(nums[idx])
        # while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
        #     idx += 1
        ret += count_sum(gap_to_target - nums[idx], idx + 1, nums, start)
        path.pop()
        idx += 1
    return ret


T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    path = []
    ret_list = []
    nums = list(map(int, input().split()))
    nums.sort()
    print(count_sum(M, 0, nums))
