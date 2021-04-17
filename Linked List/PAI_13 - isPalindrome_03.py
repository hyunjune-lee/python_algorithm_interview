# 0. 날짜 & 시도 횟수
# 2021.01.22(금요일)
# 시도 횟수 : 3 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 느리게 가는 slow러너와 빠르게가는 fast러너를 통해서 fast러너가 끝에
# 도달하는 것을 기준으로 링크드리스트의 중심부를 특정한다.
# 또한 이때 진행하면서 slow 러너는 지금까지의 링크드리스트를 rev로 만들고
# 중심부로 부터 rev, slow 를 진행시키면서 회문인지 체크한다.
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# 만약 fast가 갔는데 있는 경우는 링크드 홀수개인 경우인데 이때 slow의 위치가
# 딱 정 가운데이다. rev 가운데 직전에 위치해있다. 그렇기 때문에 한칸 더 전진시켜준다
# 1->2->3->2->1 인 경우 전진시키기 전 slow의 위치3이고 rev는 2이다.
# 짝수개인경우 1->2->2->1인경우는 slow는 뒤쪽의 2,
# rev는 앞쪽의 2에 위치하기 때문에 따로 위치 변경을 해주진 않는다
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
		slow = fast = head
		while fast and fast.next:
			fast = fast.next.next
			rev, rev.next ,slow = slow, rev ,slow.next
		if fast:
			slow = slow.next

		while rev and slow:
			if rev.val != slow.val:
				return False
			rev, slow = rev.next, slow.next
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
print(sol.isPalindrome(u.list2node([1,2,3,2,1]))) #
print(sol.isPalindrome(u.list2node([1,2,3,2,4]))) #
print(sol.isPalindrome(u.list2node([1,2,2,1]))) #
print(sol.isPalindrome(u.list2node([1,2,2,3]))) #
print(sol.isPalindrome(u.list2node([0]))) #
print(sol.isPalindrome(u.list2node([1,1]))) #
print(sol.isPalindrome(u.list2node([1,2]))) #

sol = Solution()
# print(sol.isPalindrome(1->2)) # false
