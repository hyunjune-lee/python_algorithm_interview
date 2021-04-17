# 0. 날짜 & 시도 횟수
# 2021.02.01(월요일)
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
import itertools
import copy

class Solution:
	def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
		graph = defaultdict(list)
		for a, b in prerequisites:
			graph[a].append(b)
		def dfs(node):
			if node in visited:
				return False
			visited.append(node)
			ret = True
			for next in graph[node]:
				ret = dfs(next)
			return ret

		for start in list(graph):
			visited = []
			if not dfs(start):
				return False
		return True

sol = Solution()
print(sol.canFinish(2,[[1,0]])) # True
print(sol.canFinish(2, [[1,0],[0,1]])) # False
