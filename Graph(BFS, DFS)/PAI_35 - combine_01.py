# 0. 날짜 & 시도 횟수
# 2021.01.29(금요일)
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

class Solution:
	def combine(self, n: int, k: int) -> List[List[int]]:
		ret = []
		def dfs(min):
			if len(path) == k:
				ret.append(path[:])

			for i in range(min, n+1):
				if i not in path:
					path.append(i)
					# [개선] dfs(i) => dfs(i+1)
					dfs(i+1)
					path.remove(i)
		path = []
		dfs(1)
		return ret





sol = Solution()

print(sol.combine(4,2))
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

print(sol.combine(1,1)) #  [[1]]
