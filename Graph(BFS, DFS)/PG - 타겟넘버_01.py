
def solution(numbers, target):
	global ret
	ret = 0
	def dfs(res, idx):
		if idx == len(numbers):
			global ret
			if res == target:
				ret += 1
			return
		for i in range(2):
			if i == 0:
				dfs(res - numbers[idx], idx + 1)
			else:
				dfs(res + numbers[idx], idx + 1)

	dfs(0, 0)
	return ret

print(solution([1, 1, 1, 1, 1], 3))
