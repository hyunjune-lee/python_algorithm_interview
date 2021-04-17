# 0. 날짜 & 시도 횟수
# 2021.01.22(금요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import List
from collections import *

class MyStack:

	def __init__(self):
		self.q = deque()


	def push(self, x: int) -> None:
		"""
		Push element x onto stack.
		"""


	def pop(self) -> int:
		"""
		Removes the element on top of the stack and returns that element.
		"""


	def top(self) -> int:
		"""
		Get the top element.
		"""


	def empty(self) -> bool:
		"""
		Returns whether the stack is empty.
		"""



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()






sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
