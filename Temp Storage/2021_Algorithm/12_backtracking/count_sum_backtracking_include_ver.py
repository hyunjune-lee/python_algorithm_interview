def promising(nums, cur_total, left_total, target_num, idx):
    return cur_total + left_total >= target_num and (cur_total == target_num or cur_total + nums[idx] <= target_num)


def count_sum(nums, include, cur_total, left_total, target_num, idx):
    if promising(nums, cur_total, left_total, target_num, idx):
        if cur_total == target_num:
            print(include)
        else:
            include[idx] = True
            left_total -= nums[idx]
            count_sum(nums, include, cur_total + nums[idx], left_total, target_num, idx + 1)
            include[idx] = False
            count_sum(nums, include, cur_total, left_total, target_num, idx + 1)


t = int(input())
for _ in range(t):
    target_num, n = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    include = [False for _ in range(n)]
    print(count_sum(nums, include, 0, sum(nums), target_num, 0))
