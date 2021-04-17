# 0. 날짜 & 시도 횟수
# 2021.01.31(일요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import *
from collections import *
import heapq
import itertools

class Solution:
	def subsets(self, nums: List[int]) -> List[List[int]]:
		ret = []
		len_nums = len(nums)
		def dfs(path, start):
			ret.append(path[:])

			for i in range(start, len_nums):
				if start<=i  and nums[i] not in path:
					path.append(nums[i])
					dfs(path, i+1)
					path.pop()

		dfs([], 0)
		return ret


sol = Solution()
print(sol.subsets([1,2,3])) # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(sol.subsets([0])) # [[],[0]]
