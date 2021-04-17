# 0. 날짜 & 시도 횟수
# 2021.01.16(토요일)
# 시도 횟수 : 3 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import *
from collections import *
import sys
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		min_v = sys.maxsize
		max_profit = 0
		for p in prices:
			min_v = min(min_v, p)
			max_profit = max(max_profit, p - min_v)
		return max_profit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4])) # 5
print(sol.maxProfit([7,6,4,3,1])) # 0
print(sol.maxProfit([2,4,1])) # 2
print(sol.maxProfit([7,2,4,1])) # 2
