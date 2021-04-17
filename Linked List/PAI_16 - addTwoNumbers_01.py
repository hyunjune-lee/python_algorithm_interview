# 0. 날짜 & 시도 횟수
# 2021.01.21(목요일)
# 시도 횟수 : 1 번째
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


from typing import *
from collections import *

class Solution:
	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		if (not l1) and l2:
			l1, l2 = l2, l1
		if l1:
			if l2:
				l1.val += l2.val
				if l1.val >= 10:
					l1.val -= 10
					if l1.next:
						l1.next.val += 1
					else:
						l1.next = ListNode(1, None)
				l1.next = self.addTwoNumbers(l1.next, l2.next)
			else:
				if l1.val >= 10:
					l1.val -= 10
					if l1.next:
						l1.next.val += 1
					else:
						l1.next = ListNode(1, None)
				l1.next = self.addTwoNumbers(l1.next, None)
		return l1







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
print(u.node2list(sol.addTwoNumbers(u.list2node([9,9,9,9,9,9,9]),u.list2node([9,9,9,9])))) # 5
