from typing import List


def optimal_find_max_and_min(nums: List[int], n: int) -> List[int]:
	# 1개이면 이게 가장 큰 수인 동시에 작은 수이다.
	if n == 1:
		return [nums[0], nums[0]]
	is_odd = True if n % 2 == 1 else False
	if is_odd:
		max_num =  min_num = nums[0]
	else:
		max_num, min_num = (nums[0], nums[1]) if nums[0] > nums[1] else (nums[1], nums[0])
	# 홀수이면 1부터, 짝수이면 2부터
	start = 1 if is_odd else 2
	for i in range(start, n - 1, 2):
		if nums[i] < nums[i + 1]:
			if nums[i] < min_num:
				min_num = nums[i]
			if nums[i+1] > max_num:
				max_num = nums[i+1]
		else:
			if nums[i+1] < min_num:
				min_num = nums[i+1]
			if nums[i] > max_num:
				max_num = nums[i]

	return [max_num, min_num]

T = int(input())
for _ in range(T):
	n = int(input())
	nums = list(map(int, input().split()))
	print(' '.join(map(str, optimal_find_max_and_min(nums, n))))
