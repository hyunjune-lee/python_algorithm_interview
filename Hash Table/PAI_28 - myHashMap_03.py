# 0. 날짜 & 시도 횟수
# 2021.01.28(목요일)
# 시도 횟수 : 3 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#
# 4. ref => defaultdict 사용하기

from typing import *
from collections import *

# Definition for singly-linked list.
class ListNode:
	def __init__(self, key = None, val=0, next=None):
		self.key = key
		self.val = val
		self.next = next


class MyHashMap:
	def __init__(self):
		self.size = 8000
		self.hash_table = [None] * self.size



	def put(self, key: int, value: int) -> None:
		hash_key = key % self.size
		if not self.hash_table[hash_key]:
			self.hash_table[hash_key] = ListNode(key, value)
		else:
			node = self.hash_table[hash_key]
			while node.next:
				if node.key == key:
					node.val = value
					return
				node = node.next
			if node.key == key:
				node.val = value
				return
			node.next = ListNode(key, value)





	def get(self, key: int) -> int:
		hash_key = key % self.size
		if not self.hash_table[hash_key]:
			return -1
		else:
			node = self.hash_table[hash_key]
			while node:
				if node.key == key:
					return node.val
				node = node.next
			return -1

	def remove(self, key: int) -> None:
		hash_key = key % self.size
		if self.hash_table[hash_key]:
			prev = node = self.hash_table[hash_key]
			if node.key == key:
				self.hash_table[hash_key] = node.next
				return
			node = node.next
			while node:
				if node.key == key:
					prev.next = node.next
					return
				node = node.next
				prev = prev.next




# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


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
print(u.node2list(sol.mergeKLists([u.list2node([1,4,5]),u.list2node([1,3,4]),u.list2node([2,6])])))
print(u.node2list(sol.mergeKLists([[]])))
