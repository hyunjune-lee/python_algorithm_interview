# 0. 날짜 & 시도 횟수
# 2021.02.03(수요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 트리의 한 레벨마다 노드를 가져와서 역순으로 바꿔서 다시 넣어주었다.
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)

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
		new_Q = deque([root])
		while Q:
			level_len = len(Q)
			for _ in range(level_len):
				node = Q.popleft()
				if node:
					Q.append(node.left)
					Q.append(node.right)
			new_level = list(Q)[:]
			for _ in range(level_len):
				new_node = new_Q.popleft()
				if new_node:
					new_node.left = new_level.pop()
					new_Q.append(new_node.left)
					new_node.right = new_level.pop()
					new_Q.append(new_node.right)
		return root





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
