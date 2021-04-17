# 0. 날짜 & 시도 횟수
# 2021.02.04(목요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# return max(left, right) 할때 +1 안 해줌
# 나는 중간에 ans 최대값을 체크하지 않았는데 이는 무조건 가운데 루트를 지나서
# 직경이 정해질거라고 생각했기 때문이다. 하지만 생각해보면 루트를 지나치지 않은 채
# 한 쪽 서브트리에서 가장 긴 경로가 나올 수 있다. 그렇기 때문에 self.ans를 이용해 높이를 체크해야 한다.

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
	def diameterOfBinaryTree(self, root: TreeNode) -> int:
		self.ans = 1
		def depth(node: TreeNode) -> int:
			if not node:
				return 0
			left = depth(node.left)
			right = depth(node.right)
			self.ans = max(self.ans, left+right + 1)
			return max(left, right) + 1
		depth(root)
		return self.ans - 1

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
# print(sol.diameterOfBinaryTree(U.list_to_tree([1,2,3,4,5]))) # 3
print(sol.diameterOfBinaryTree(U.list_to_tree([4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]))) # 8
