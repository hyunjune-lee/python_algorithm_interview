def counting_inv(nums):
    if len(nums) == 1:
        return nums
    mid = len(nums) // 2
    low_nums = counting_inv(nums[:mid])
    high_nums = counting_inv(nums[mid:])
    l = h = 0
    merged_arr = []
    while l < len(low_nums) and h < len(high_nums):
        if low_nums[l] <= high_nums[h]:
            merged_arr.append(low_nums[l])
            l += 1
        else:
            global inv_count
            inv_count += len(low_nums) - l
            merged_arr.append(high_nums[h])
            h += 1
    merged_arr.extend(low_nums[l:])
    merged_arr.extend(high_nums[h:])

    return merged_arr


inv_count = 0
for _ in range(int(input())):
    N = int(input())
    nums = list(map(int, input().split()))
    inv_count = 0
    counting_inv(nums)
    print(inv_count)
