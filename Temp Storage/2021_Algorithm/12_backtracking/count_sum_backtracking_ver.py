def promising(nums, cur_total, left_total, target_num, idx):
    return cur_total + left_total >= target_num and (cur_total == target_num or cur_total + nums[idx] <= target_num)


def count_sum(nums, cur_total, left_total, target_num, idx):

    if promising(nums, cur_total, left_total, target_num, idx):

        if cur_total == target_num:
            global sum_case_count
            sum_case_count += 1
        else:
            left_total -= nums[idx]  # 상태 트리에서 지나치면 다시 넣을 수 없기 때문에 left_total이 줄어들 수 밖에 없음
            count_sum(nums, cur_total + nums[idx], left_total, target_num, idx + 1)
            count_sum(nums, cur_total, left_total, target_num, idx + 1)


t = int(input())
for _ in range(t):
    target_num, n = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    sum_case_count = 0
    count_sum(nums, 0, sum(nums), target_num, 0)
    print(sum_case_count)
