# 0. 날짜 & 시도 횟수
# 2021.02.04(목요일)
# 시도 횟수 : 3 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 재귀를 통해서 깊이를 구했다.
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
		if root is None:
			return 0
		left = self.maxDepth(root.left)
		right = self.maxDepth(root.right)
		depth = max(left, right) + 1
		return depth







sol = Solution()
print(sol.maxDepth([3,9,20,None,None,15,7])) # True
print(sol.maxDepth([1,None,2])) # False
