# 0. 날짜 & 시도 횟수
# 2021.01.21(목요일)
# 시도 횟수 : 2 번째
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
	def isPalindrome(self, head: ListNode) -> bool:
		rev = None
		fast = slow = head

		while fast and fast.next:
			fast = fast.next.next
			rev, rev.next, slow = slow, rev, slow.next
		if fast:
			slow = slow.next

		while slow:
			if slow.val != rev.val:
				return False
			rev = rev.next
			slow = slow.next
		return True


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
print(sol.isPalindrome(u.list2node([1,2,3,2,4]))) #

sol = Solution()
# print(sol.isPalindrome(1->2)) # false
