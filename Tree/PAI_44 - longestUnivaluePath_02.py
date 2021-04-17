# 0. 날짜 & 시도 횟수
# 2021.02.04(목요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# 재귀부분을 dfs 부분에 넣어놓고 막상 left = dfs(node.left)로 해야되는데
# 여전히 left = longestUnivaluePath(node.left) 이렇게 했다.
# 이것도 경로이기 때문에 res 부분은 self.res = max(self.res, left + right) 이렇게 left+right이지만
# 반환하는 것 left+right가 아닌 max(left, right)이여야 한다.  return max(left, right)

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
	res = 0
	def longestUnivaluePath(self, root: TreeNode) -> int:
		def dfs(node):
			if not node:
				return 0
			left = dfs(node.left)
			if node.left and node.val == node.left.val:
				left += 1
			else:
				left = 0
			right = dfs(node.right)
			if node.right and node.val == node.right.val:
				right += 1
			else:
				right = 0
			self.res = max(self.res, left + right)
			return max(left, right)
		self.res = 0
		dfs(root)
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
# print("res: ",sol.longestUnivaluePath(U.list_to_tree([5,4,5,1,1,5]))) # 2
# print("res: ",sol.longestUnivaluePath(U.list_to_tree([1,4,5,4,4,5]))) # 2
print(sol.longestUnivaluePath(U.list_to_tree([1,None,1,1,1,1,1,1]))) # 4
