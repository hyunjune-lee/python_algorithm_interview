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
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		ret = []
		path = []
		def dfs(start):
			sum_path = sum(path)
			if sum_path > target:
				return
			elif sum_path == target:
				ret.append(path[:])
				return

			for idx, num in enumerate(candidates):
				if idx >= start:
					path.append(num)
					dfs(idx)
					path.pop()
		dfs(0)
		return ret




sol = Solution()

print(sol.combinationSum([2,3,6,7],7)) # [[2,2,3],[7]]
print(sol.combinationSum([2,3,5],8)) #  [[2,2,2,2],[2,3,3],[3,5]]
print(sol.combinationSum([2],1)) # []
