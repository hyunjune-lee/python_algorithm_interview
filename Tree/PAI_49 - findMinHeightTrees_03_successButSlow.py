# 0. 날짜 & 시도 횟수
# 2021.02.07(일요일)
# 시도 횟수 : 3 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# 그래프에서 리프노드를 제거할때 한번에 모든 리프노드를 제거해야되는데
# 나는 자칫하면 리프노드를 제거해서 리프노드가 된 노드를 연속으로 제거하게 해주었다.

from typing import *
from collections import *
import heapq
import itertools
import copy

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
		if not edges:
			return [0]
		dic = defaultdict(list)
		for a, b in edges:
			dic[a].append(b)
			dic[b].append(a)
		node_list = list(dic.keys())
		while len(node_list) > 2:
			remove_list = []
			next_node_list = node_list[:]
			for node in node_list:
				if len(dic[node]) == 1:
					con = dic[node].pop()
					next_node_list.remove(node)
					remove_list.append((con,node))
			node_list = next_node_list
			for con, node in remove_list:
				dic[con].remove(node)

		return node_list










class Utility:
	def list_to_tree(self, l: List[int]) -> TreeNode:
		if not l:
			return None
		root = TreeNode(l.pop(0))
		Q = deque([root])
		while Q:
			node = Q.popleft()
			if l:
				node.left = TreeNode(l.pop(0))
				Q.append(node.left)
			if l:
				node.right = TreeNode(l.pop(0))
				Q.append(node.right)
		return root





sol = Solution()
U = Utility()

print(sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])) #[1]
print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) #[3, 4]
print(sol.findMinHeightTrees(1, [])) #[0]
print(sol.findMinHeightTrees(2, [[0,1]])) #[0, 1]
print(sol.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])) #[3]
