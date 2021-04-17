# 0. 날짜 & 시도 횟수
# 2021.01.24(일요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import List
from collections import *

class MyQueue:

	def __init__(self):
		self.stack = []



	def push(self, x: int) -> None:
		"""
		Push element x to the back of queue.
		"""
		temp_stack = []
		while self.stack:
			temp_stack.append(self.stack.pop())
		self.stack.append(x)
		while temp_stack:
			self.stack.append(temp_stack.pop())


	def pop(self) -> int:
		"""
		Removes the element from in front of queue and returns that element.
		"""
		return self.stack.pop()


	def peek(self) -> int:
		"""
		Get the front element.
		"""
		return self.stack[-1]


	def empty(self) -> bool:
		"""
		Returns whether the queue is empty.
		"""
		return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()






sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
