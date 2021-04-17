# 0. 날짜 & 시도 횟수
# 2021.02.07(일요일)
# 시도 횟수 : 3 번째(O - 92ms(98.79%))
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 직렬화할때는 bfs 방식으로 노드를 꺼내고 노드가 있으면 left, right를 Q에 넣고 그 노드를 결과 리스트에 넣는다.
# 만약 노드가 없으면 None을 넣는다
# 역직렬화할때는 Q에서 노드를 꺼내서 left,right에 노드를 만들어서 붙여준다.(이때 데이터 리스트에 popleft해서)
# 없으면 그냥 넘어간다.
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



	def deserialize(self, data):
		if not data:
			return None
		data_queue = deque(data)
		root  = TreeNode(data_queue.popleft())
		Q = deque([root])
		while Q:
			node = Q.popleft()
			left = data_queue.popleft()
			if node and left is not None:
					node.left = TreeNode(left)
					Q.append(node.left)
			right = data_queue.popleft()
			if node and right is not None:
					node.right = TreeNode(right)
					Q.append(node.right)

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
print(sol.serialize(sol.deserialize(sol.serialize(U.list_to_tree( [])))))
