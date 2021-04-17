
# 0. 날짜 & 시도 횟수
# 2021.01.15(금요일)
# 시도 횟수 : 1 번째
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
		min_i = prices.index(min(prices))
		max_i = prices.index(max(prices))
		ret_by_max = (prices[max_i] - min(prices[:max_i])) if len(prices[:max_i]) !=0 else 0
		ret_by_min = (max(prices[min_i+1:]) - prices[min_i]) if len(prices[min_i+1:]) !=0 else 0
		return max(ret_by_min, ret_by_max)

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4])) # 5
print(sol.maxProfit([7,6,4,3,1])) # 0
print(sol.maxProfit([2,4,1])) # 2
