# # 0. 날짜 & 시도 횟수
# # 2021.02.03(수요일)
# # 시도 횟수 : 1 번째
# # 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# #
# # 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# #
# # 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# #  길이를 통해서 깊이를 재려고 했지만 돌려보니 이진트리의 루트 노드를 돌려주는 것이라 이 로직은 불가능함..

# from typing import *
# from collections import *
# import heapq
# import itertools
# import copy

# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
# 	def maxDepth(self, root: TreeNode) -> int:
# 		dfs

# 		tree_len = len(root)
# 		depth = 0
# 		two_power = 1
# 		power_sum = 0
# 		while tree_len > power_sum:
# 			power_sum += two_power
# 			two_power *= 2
# 			depth += 1
# 		return depth






# sol = Solution()
# print(sol.maxDepth([3,9,20,None,None,15,7])) # True
# print(sol.maxDepth([1,None,2])) # False
