# 0. 날짜 & 시도 횟수
# 2021.02.03(수요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# dfs내에서의 구조를 구축하지 못했다.

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
		if t1 and t2 and t1.val and t2.val:
			t1.val += t2.val
			self.mergeTrees(t1.left, t2.left)
			self.mergeTrees(t1.right, t2.right)
		elif t2 and t2.val:
			t1 = TreeNode(t2.val)
			self.mergeTrees(None, t2.left)
			self.mergeTrees(None, t2.right)
		elif t1 and t1.val:
			self.mergeTrees(t1.left, None)
			self.mergeTrees(t1.right, None)
		else:
			return None
		return t1









		# new_node = new_root = None
		# t1_Q = deque([t1])
		# t2_Q = deque([t2])
		# while t1_Q or t2_Q:
		# 	node_t1 = t1_Q.popleft()
		# 	node_t2 = t2_Q.popleft()
		# 	new_node





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
