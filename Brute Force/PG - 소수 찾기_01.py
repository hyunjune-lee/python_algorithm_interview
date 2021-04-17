def solution(numbers):
	path = []
	idx_check = []
	can_set = set()
	def dfs(nums):
		if path:
			can_set.add(int(''.join(path)))
		for idx, n in enumerate(nums):
			if idx not in idx_check:
				path.append(n)
				idx_check.append(idx)
				dfs(nums)
				path.pop()
				idx_check.pop()
	answer = 0
	int_nums = []

	for n in numbers:
		int_nums.append(int(n))

	dfs(numbers)
	for can in can_set:
		if can > 1:
			is_prime = 1
			for div in range(2, can -1):
				if can % div == 0:
					is_prime = 0
					break
			if is_prime == 1:
				answer +=1

	return answer


print(solution("17"))
print(solution("011"))
