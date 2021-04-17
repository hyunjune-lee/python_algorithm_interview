# 0. 날짜 & 시도 횟수
# 2021.02.03(수요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 한 레벨에서 bfs가 돌때마다 깊이를 더해줘서 최종 깊이를 반환
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# 한 레벨씩 돌릴때 len(queue) 만큼 for문 도는것
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import *
from collections import *
import heapq
import itertools
import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		if not root:
			return 0

		q = deque([root])
		depth = 0
		while q:
			depth += 1
			for _ in range(len(q)):
				cur_root = q.popleft()
				if cur_root.left:
					q.append(cur_root.left)
				if cur_root.right:
					q.append(cur_root.right)
		return depth

class Utility:
	def list_to_tree(self, l: List[int]) -> TreeNode:
		if not l:
			return None
		count = len(l)
		root = TreeNode(l.pop(0))
		Q = deque([root])
		while Q and count > 0:
			if count > 0:
				node = Q.popleft()
				count -= 1
			if count > 0:
				node.left = TreeNode(l.pop(0))
				Q.append(node.left)
				count -= 1
			if count > 0:
				node.right = TreeNode(l.pop(0))
				Q.append(node.left)
				count -= 1
		return root



sol = Solution()
U = Utility()
print(sol.maxDepth(U.list_to_tree([3,9,20,None,None,15,7]))) # True
print(sol.maxDepth(U.list_to_tree([1,None,2]))) # True
