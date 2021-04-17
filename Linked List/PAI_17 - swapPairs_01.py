# 0. 날짜 & 시도 횟수
# 2021.01.21(목요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 현재노드와 다음노드의 값을 스왑하고 현재노드에서 다음다음 노드로 이동한다.
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
	def swapPairs(self, head: ListNode) -> ListNode:
		node = head
		while node and node.next:
			node.val, node.next.val = node.next.val, node.val
			node = node.next.next
		return head


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
print(u.node2list(sol.swapPairs(u.list2node([1,2,3,4])))) # [2, 1, 4, 3]
print(u.node2list(sol.swapPairs(u.list2node([1,2,3,4,5])))) # 5
print(u.node2list(sol.swapPairs(u.list2node([])))) # 5
print(u.node2list(sol.swapPairs(u.list2node([1])))) # 5
