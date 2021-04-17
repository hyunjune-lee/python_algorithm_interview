# 0. 날짜 & 시도 횟수
# 2021.02.02(화요일)
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
	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
		graph = defaultdict(list)
		for u, v, price in flights:
			graph[u].append((v,price))

		Q = [(0, src, K)]
		while Q:
			price, node, k = heapq.heappop(Q)
			if k >=0:
				if node == dst:
					return price
				for next_p, next_node in graph[node]:
					heapq.heappush(Q, (price + next_p, next_node, k -1))

		return -1












sol = Solution()
print(sol.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]],0,2,1)) # 200
print(sol.findCheapestPrice(3,  [[0,1,100],[1,2,100],[0,2,500]], 0, 2,0)) # 500
print(sol.findCheapestPrice(4,  [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3,1)) # 6
