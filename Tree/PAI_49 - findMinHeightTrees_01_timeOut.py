# 0. 날짜 & 시도 횟수
# 2021.02.05(금요일)
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

# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Solution:
	def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
		# 사전에 넣기
		dic = defaultdict(list)
		for a,b in edges:
			dic[a].append(b)
			dic[b].append(a)
		depth_dic = defaultdict(list)
		for i in range(n):
			Q = deque([i])
			depth = 0
			# 중복체크
			path = []
			while Q:
				depth += 1
				for _ in range(len(Q)):
					node = Q.popleft()
					path.append(node)
					for con in dic[node]:
						if con not in path:
							Q.append(con)
			depth_dic[depth].append(i)

		return sorted(depth_dic.items())[0][1]














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

print(sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(sol.findMinHeightTrees(1, []))
print(sol.findMinHeightTrees(2, [[0,1]]))
