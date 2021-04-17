# 0. 날짜 & 시도 횟수
# 2021.02.07(일요일)
# 시도 횟수 : 2 번째
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
	res : bool = True
	def isBalanced(self, root: TreeNode) -> bool:
		def depth(node):
			if not node or node.val == None:
				return 0
			left = depth(node.left)
			right = depth(node.right)
			if abs(left - right) > 1:
				self.res = False
			return max(left, right) + 1
		self.res = True
		depth(root)
		return self.res













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
# print(sol.isBalanced(U.list_to_tree([3,9,20,None,None,15,7]))) # true
print(sol.isBalanced(U.list_to_tree([1,2,2,3,3,None,None,4,4]))) # false
# print(sol.isBalanced(U.list_to_tree([2,1,3,0,7,9,1,2,None,1,0,None,None,8,8,None,None,None,None,7]))) # true
