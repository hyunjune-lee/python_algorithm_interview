# 0. 날짜 & 시도 횟수
# 2021.01.23(토요일)
# 시도 횟수 : 3 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
		root = start = ListNode(None)
		start.next = head
		for _ in range(m -1):
			start = start.next
		node = start.next
		for _ in range(n - m):
			tmp = start.next
			start.next  =node.next
			start.next.next, node.next = tmp,  node.next.next
		return root.next












from typing import *
from collections import *


class Utility:
	def node2list(self, node1: ListNode) -> List: #linked list -> list
		list1 = []
		while node1 != None :
			list1.append(node1.val)
			node1 = node1.next
		return list1

	def list2node(self, list1: List) -> ListNode:
		result_node = ListNode()

		for i,num in enumerate(list1):
			if i == 0 :
				result_node.val = num
			else :
				node = result_node
				while node.next != None:
					node = node.next
				node.next = ListNode(num)
		return result_node

sol = Solution()
u = Utility()
print(u.node2list(sol.reverseBetween(u.list2node([1,2,3,4,5]),2,4))) # 5
print(u.node2list(sol.reverseBetween(u.list2node([2,1,3,5,6,4,7]),2,4))) # 5
print(u.node2list(sol.reverseBetween(u.list2node([1,2,3,4]),2,4))) # [2, 1, 4, 3]
# print(u.node2list(sol.reverseBetween(u.list2node([])))) # 5
# print(u.node2list(sol.reverseBetween(u.list2node([1])))) # 5
