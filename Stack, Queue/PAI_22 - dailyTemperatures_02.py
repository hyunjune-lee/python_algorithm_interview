# 0. 날짜 & 시도 횟수
# 2021.01.24(일요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# stack에 index를 넣어서 연산을 하는 것
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import List
from collections import *

class Solution:
	def dailyTemperatures(self, T: List[int]) -> List[int]:
		stack = []
		ret = [0 for _ in T]
		for i, cur in enumerate(T):
			while stack and T[stack[-1]] < cur:
				before_i = stack.pop()
				ret[before_i] = i - before_i
			stack.append(i)
		return ret


sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
