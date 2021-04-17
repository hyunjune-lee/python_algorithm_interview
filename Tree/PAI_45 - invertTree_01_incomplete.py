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
	def invertTree(self, root: TreeNode) -> TreeNode:
		Q = deque([root])
		new_root = root
		new_Q = deque([new_root])
		while Q:
			level_len = len(Q)
			for _ in range(level_len):
				node = Q.popleft()
				if node:
					Q.append(node.left)
					Q.append(node.right)
			new_level = deque(list(Q)[::-1])
			new_level_len = len(new_level)
			for _ in range(level_len):
				new_node = new_Q.popleft()
				left = new_level.popleft()
				if left:
					new_node.left = TreeNode(left.val)
				else:
					new_node.left = None
				new_Q.append(new_node.left)
				right = new_level.popleft()
				if right:
					new_node.right = TreeNode(right.val)
				else:
					new_node.right = None
				new_Q.append(new_node.right)

		return new_root





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
print(sol.invertTree(U.list_to_tree([4,2,7,1,3,6,9]))) # 2
