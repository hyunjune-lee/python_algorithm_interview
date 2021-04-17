# 0. 날짜 & 시도 횟수
# 2021.01.15(금요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import *
from collections import *


class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		max_profit = 0
		len_prices = len(prices)
		min_list = []
		max_list = []
		min_v = prices[0]
		max_v = prices[-1]
		for i in range(len_prices):
			min_v = min(min_v, prices[i])
			min_list.append(min_v)
			max_v = max(max_v, prices[len_prices-1-i])
			max_list.append(max_v)
		max_list.reverse()
		for i in range(len_prices):
			max_profit = max(max_profit, max_list[i] - min_list[i])
		return max_profit


sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4])) # 5
print(sol.maxProfit([7,6,4,3,1])) # 0
print(sol.maxProfit([2,4,1])) # 2
print(sol.maxProfit([7,2,4,1])) # 2
