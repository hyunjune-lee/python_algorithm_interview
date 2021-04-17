
def solution(numbers, target):
	global ret
	ret = 0
	def dfs(res, idx):
		global ret
		if idx == len(numbers):
			if res == target:
				ret += 1
			return

		dfs(res - numbers[idx], idx + 1)
		dfs(res + numbers[idx], idx + 1)

	dfs(0, 0)
	return ret

print(solution([1, 1, 1, 1, 1], 3))
