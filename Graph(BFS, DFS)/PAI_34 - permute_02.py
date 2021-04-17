# 0. 날짜 & 시도 횟수
# 2021.01.31(일요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import *
from collections import *
import heapq

class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:
		ret = []
		prev_elements = []

		def dfs(elements):
			if len(elements) == 0:
				ret.append(prev_elements[:])

			for e in elements:
				next_elements = elements[:]
				next_elements.remove(e)

				prev_elements.append(e)
				dfs(next_elements)
				prev_elements.pop()
		dfs(nums)
		return ret









sol = Solution()

print(sol.permute([1,2,3])) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

print(sol.permute([0,1])) #  [[0,1],[1,0]]

print(sol.permute([1])) # [[1]]
