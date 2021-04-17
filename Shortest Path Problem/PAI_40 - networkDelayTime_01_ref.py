# 0. 날짜 & 시도 횟수
# 2021.02.01(월요일)
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
import copy

class Solution:
	def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
		graph = defaultdict(list)
		for u, v, w in times:
			graph[u].append((v, w))

		Q = [[(0, k)]]
		dist = defaultdict(int)
		while Q:
			time, node = heapq.heappop(Q)
			if node not in dist:
				dist[node] = time
				for v, w in graph[node]:
					alt = time + w
					heapq.heappush(Q, (alt, v))
		if len(dist) == n:
			return max(dist.values())
		return -1




sol = Solution()
print(sol.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # True
print(sol.networkDelayTime([[1,2,1]], 2, 1)) # False
