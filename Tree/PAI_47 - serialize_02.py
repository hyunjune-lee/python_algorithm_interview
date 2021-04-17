# 0. 날짜 & 시도 횟수
# 2021.02.05(금요일)
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
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Codec:

	def serialize(self, root):
		Q = deque([root])
		res = ["#"]
		while Q:
			node = Q.popleft()
			if node:
				Q.append(node.left)
				Q.append(node.right)
				res.append(str(node.val))
			else:
				res.append("#")
		return " ".join(res)


	def deserialize(self, data):
		if data == "# #":
			return None
		node_list = data.split()
		root = TreeNode(int(node_list[1]))
		Q = deque([root])
		index = 2
		while Q:
			node = Q.popleft()
			if node_list[index] != '#':
				node.left = TreeNode(int(node_list[index]))
				Q.append(node.left)
			index += 1

			if node_list[index] != '#':
				node.right = TreeNode(int(node_list[index]))
				Q.append(node.right)
			index += 1

		return root







# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))












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



sol = Codec()
U = Utility()
# print(sol.mergeTrees(U.list_to_tree([1,3,2,5]), U.list_to_tree([2,1,3,None,4,None,7]))) # 2
print(sol.serialize(U.list_to_tree( [1,2,3,None,None,4,5])))
print(sol.deserialize(sol.serialize(U.list_to_tree( [1,2,3,None,None,4,5]))))
print(sol.serialize(sol.deserialize(sol.serialize(U.list_to_tree( [1,2,3,None,None,4,5])))))
