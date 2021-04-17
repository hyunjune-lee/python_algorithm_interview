# 0. 날짜 & 시도 횟수
# 2021.02.07(일요일)
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
	add_sum = 0
	def bstToGst(self, root: TreeNode) -> TreeNode:
		def run(node) -> int:
			if not node or node.val is None:
				return 0
			run(node.right)
			self.add_sum += node.val
			node.val = self.add_sum
			run(node.left)
			return self.add_sum
		self.add_sum = 0
		run(root)
		return root

# class Solution:
# 	add_sum = 0
# 	def bstToGst(self, root: TreeNode) -> TreeNode:
# 		def run(node) -> int:
# 			if not node or node.val is None:
# 				return 0

# 			right_val = run(node.right)

# 			node.val += right_val
# 			if node.left and node.left.val is not None:
# 				node.left.val += node.val
# 				left_val = run(node.left)
# 				return left_val
# 			return node.val
# 		run(root)
# 		return root









class Utility:
	def serialize(self, root):
		if not root:
			return []
		Q = deque([root])
		ret = []
		while Q:
			node = Q.popleft()
			if node:
				Q.append(node.left)
				Q.append(node.right)
				ret.append(node.val)
			else:
				ret.append(None)
		return ret

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

print(U.serialize(sol.bstToGst(U.list_to_tree([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8])))) #[1]
