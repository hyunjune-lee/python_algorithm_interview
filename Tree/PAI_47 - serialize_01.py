# 0. 날짜 & 시도 횟수
# 2021.02.04(목요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# serialize에서 node.left와 right를 따로 넣어줄 필요 없이 어차피 Q 돌면서 다 순회하기 때문에
# node 부분에서 한번만 하면 된다.



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
		S = [root.val]
		while Q:
			len_Q = len(Q)
			for _ in range(len_Q):
				node  = Q.popleft()
				if node.left:
					Q.append(node.left)
					S.append(node.left.val)
				else:
					S.append(None)
				if node.right:
					Q.append(node.right)
					S.append(node.right.val)
				else:
					S.append(None)

		idx = len(S) - 1
		while S[idx] is None and idx >=0 :
			idx -= 1
		return S[:idx+1]


	# [1,2,3,null,null,4,5]
	# 1 나오면 길이를 재고 길이 1 마다 두번의 popleft => left ,right,
	# 그리고 이 노드들 다시 큐에다가 넣기
	def deserialize(self, data):
		if not data:
			return None
		D = deque(data)
		root = TreeNode(D.popleft())
		Q = deque([root])
		while Q:
			node = Q.popleft()
			if D and node:
				node.left = TreeNode(D.popleft())
				if node.left.val == None:
					node.left = None
				Q.append(node.left)
			if D and node:
				node.right = TreeNode(D.popleft())
				if node.right.val == None:
					node.right = None
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
		l = list(data)
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
