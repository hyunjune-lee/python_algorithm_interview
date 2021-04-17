# 0. 날짜 & 시도 횟수
# 2021.02.04(목요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# 			if n1 and n2: 이때 조건에 and n1.val n2.val 이렇게도 넣었는데
# 음수끼리의 합에서 제대로 연산이 되지 않았다. val 관련 조건을 삭제 후 정상작동함
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
	def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		def dfs(n1, n2):
			if not n1 and not n2 :
				return None
			if n1 and n2:
				node = TreeNode(n1.val + n2.val)
				node.left = dfs(n1.left, n2.left)
				node.right = dfs(n1.right, n2.right)
				return node
			if n1:
				return n1
			if n2:
				return n2

		return dfs(t1, t2)












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
print(sol.mergeTrees(U.list_to_tree([1,3,2,5]), U.list_to_tree([2,1,3,None,4,None,7]))) # 2
