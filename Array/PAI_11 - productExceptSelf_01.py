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
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		ret = [1 for i in nums]
		for i, v in enumerate(nums[:-1]):
			for j,x in enumerate(nums[i+1:]):
				ret[i] *= x
				ret[i+1+j] *= v
		return ret




sol = Solution()

print(sol.productExceptSelf([1,2,3,4])) # [24,12,8,6]
