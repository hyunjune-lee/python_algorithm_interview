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
	longest_path = 0
	def longestUnivaluePath(self, root: TreeNode) -> int:

		def dfs(node : TreeNode, parent_val) -> int:
			if not node:
				return 0
			left = dfs(node.left, node.val)
			right = dfs(node.right, node.val)
			self.longest_path = max(self.longest_path, left + right)
			if node.val == parent_val:
				return left + right + 1
			return 0
		self.longest_path = 0
		dfs(root, None)
		return self.longest_path





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
print(sol.longestUnivaluePath(U.list_to_tree([5,4,5,1,1,5]))) # 2
print(sol.longestUnivaluePath(U.list_to_tree([1,4,5,4,4,5]))) # 2
print(sol.longestUnivaluePath(U.list_to_tree([1,None,1,1,1,1,1,1]))) # 4
