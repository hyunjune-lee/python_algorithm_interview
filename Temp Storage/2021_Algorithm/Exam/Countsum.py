def count_sum(gap_to_target, idx, nums):
    if gap_to_target < 0:
        return 0
    elif gap_to_target == 0:
        ret_list.append(path[:])
        return 1
    ret = 0
    for i in range(idx, len(nums)):
        path.append(nums[i])
        ret += count_sum(gap_to_target - nums[i], i + 1, nums)
        path.pop()
    return ret


T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    path = []
    ret_list = []
    nums = list(map(int, input().split()))
    count_sum(M, 0, nums)
    ret_set = set()
    for ret in ret_list:
        ret.sort()
        ret_set.add(tuple(ret))
    print(len(ret_set))
