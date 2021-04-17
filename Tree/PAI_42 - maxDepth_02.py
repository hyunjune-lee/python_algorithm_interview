# 0. 날짜 & 시도 횟수
# 2021.02.03(수요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#  탐색을 진행할 때 node뿐 아니라 bfs가 작동한 횟수도 같이 튜플로 넣어서 탐색 진행
# 탐색 진행시마다 자식 노드는 현재 부모 노드의 깊이보다 1개 더 깊게 설정함
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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
	def maxDepth(self, root: TreeNode) -> int:
		if not root:
			return 0

		q = deque([(root, 1)])
		max_depth = 0
		while q:
			node, depth = q.popleft()
			max_depth = max(depth, max_depth)
			if node.left:
				q.append((node.left, depth + 1))
			if node.right:
				q.append((node.right, depth + 1))
		return max_depth





sol = Solution()
print(sol.maxDepth([3,9,20,None,None,15,7])) # True
print(sol.maxDepth([1,None,2])) # False
