# 0. 날짜 & 시도 횟수
# 2021.01.31(일요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# 중간에 tic 처리를 할때 i번째에 있는 요소를 제거하고 리스트 뒤에 append를 해주었다.
# 이때문에 dfs루프 안에서 if문을 두번 체크할 때 순서가 변경된 리스트에서 제거하기 때문에
# 원치않은 결과가 발생하게 된다.
# 2. deepcopy 안해줌


from typing import *
from collections import *
import heapq
import itertools
import copy
class Solution:
	def findItinerary(self, tickets: List[List[str]]) -> List[str]:
		if not tickets:
			return
		def dfs(next, path, d):
			if ret:
				return
			if len(path) == len(tickets) + 1:
				ret.append(path[:])
				return
			new_dic = d.copy()
			for n in d[next]:
				new_dic = copy.deepcopy(d)
				new_dic[next].remove(n)
				path.append(n)
				dfs(n, path, new_dic)
				path.pop()

		dic = defaultdict(list)
		for ticket in tickets:
			dic[ticket[0]].append(ticket[1])
		for ticket in tickets:
			dic[ticket[0]].sort()

		ret = []
		start = ['JFK']
		for next in dic['JFK']:
			new_dic = copy.deepcopy(dic)
			new_dic['JFK'].remove(next)
			start.append(next)
			dfs(next, start, dic)
			start.pop()
		return ret[0]


sol = Solution()
print(sol.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
#["JFK", "MUC", "LHR", "SFO", "SJC"]
print(sol.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
#  ["JFK","ATL","JFK","SFO","ATL","SFO"]
print(sol.findItinerary([["JFK","ATL"],["ATL","JFK"]]))
# ["JFK","ATL","JFK"]
print(sol.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]))
