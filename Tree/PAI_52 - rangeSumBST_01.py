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
	range_sum = 0
	def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
		def range_search(node):
			if not node or node.val is None:
				return
			range_search(node.left)
			if low <= node.val <= high:
				self.range_sum += node.val
			if high < node.val:
				return
			range_search(node.right)
			return
		self.range_sum = 0
		range_search(root)
		return self.range_sum


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

print(sol.rangeSumBST(U.list_to_tree([10,5,15,3,7,None,18]), 7 ,15)) # 32
print(sol.rangeSumBST(U.list_to_tree([10,5,15,3,7,13,18,1,None,6]), 6 ,10)) # 23
