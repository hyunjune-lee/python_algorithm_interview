# 0. 날짜 & 시도 횟수
# 2021.02.05(금요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# 리프노드는 연결된게 1개 밖에 없다.
# ref 참고 결과 => 삭제할 리프 노드들을 leaves라는 리스트에 넣어주고
# 이 leaves만 삭제 그리고 삭제해서 리프노드가 된 노드들을 new_leaves에 넣어준다
# 그리고 new_leaves를 leaves로 변경해주었다.
# # 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# 그래프에서 리프노드를 제거할때 한번에 모든 리프노드를 제거해야되는데
# 나는 자칫하면 리프노드를 제거해서 리프노드가 된 노드를 연속으로 제거하게 해주었다.


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
	def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
		if n <= 1:
			return [0]

		graph = defaultdict(list)
		for i, j in edges:
			graph[i].append(j)
			graph[j].append(i)

		leaves = []
		for i in range(n + 1):
			if len(graph[i]) == 1:
				leaves.append(i)

		while n > 2:
			n -= len(leaves)
			new_leaves = []
			for leaf in leaves:
				neighbor = graph[leaf].pop(0)
				graph[neighbor].remove(leaf)

				if len(graph[neighbor]) == 1:
					new_leaves.append(neighbor)

			leaves = new_leaves
		return leaves














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

print(sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])) #[1]
print(sol.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])) #[3, 4]
print(sol.findMinHeightTrees(1, [])) #[0]
print(sol.findMinHeightTrees(2, [[0,1]])) #[0, 1]
print(sol.findMinHeightTrees(6, [[0,1],[0,2],[0,3],[3,4],[4,5]])) #[3]
