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

class Solution:
	def dailyTemperatures(self, T: List[int]) -> List[int]:
		ret = [0 for _ in T]
		stack = []

		for idx, temp in enumerate(T) :
			while stack and temp > stack[-1][0]:
				before_idx = stack.pop()[1]
				ret[before_idx] = idx - before_idx
			stack.append((temp, idx))
		return ret






sol = Solution()
print(sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
