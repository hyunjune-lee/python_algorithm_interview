# 0. 날짜 & 시도 횟수
# 2021.01.16(토요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

# Definition for singly-linked list.

from typing import *
from collections import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		l1_node = l1
		l2_node = l2
		new_head = ListNode()
		new_node = new_head
		while l1_node is not None and l2_node is not None:
			if l1_node.val < l2_node.val:
				new_node.next = ListNode(l1_node.val)
				l1_node = l1_node.next
			else:
				new_node.next = ListNode(l2_node.val)
				l2_node = l2_node.next
			new_node = new_node.next
		while l1_node is not None:
			new_node.next = ListNode(l1_node.val)
			l1_node = l1_node.next
			new_node = new_node.next
		while l2_node is not None:
			new_node.next = ListNode(l2_node.val)
			l2_node = l2_node.next
			new_node = new_node.next
		return new_head.next

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
print(u.node2list(sol.mergeTwoLists(u.list2node([1,2,4]),u.list2node([1,3,4])))) # 5
