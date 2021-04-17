# 0. 날짜 & 시도 횟수
# 2021.02.01(월요일)
# 시도 횟수 : 3 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# 언어순으로 할 때 정렬을 미리하는 것


from typing import *
from collections import *
import heapq
import itertools
import copy
class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		graph = defaultdict(list)
		for a, b in sorted(tickets):
			graph[a].append(b)
		route = []
		def dfs(a):
			while graph[a]:
				dfs(graph[a].pop(0))
			route.append(a)

		dfs('JFK')
		return route[::-1]


sol = Solution()
# print(sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# #["JFK", "MUC", "LHR", "SFO", "SJC"]
# print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# #  ["JFK","ATL","JFK","SFO","ATL","SFO"]
# print(sol.findItinerary([["JFK","ATL"],["ATL","JFK"]]))
# ["JFK","ATL","JFK"]
print(sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
# ['JFK', 'NRT', 'JFK', 'KUL']
