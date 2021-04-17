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

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		l_mul = [1 for _ in nums]
		r_mul = [1 for _ in nums]
		len_nums = len(nums)
		for i in range(1, len_nums):
			l_mul[i] = l_mul[i - 1] * nums[i-1]
			r_i = len_nums - 1
			r_mul[r_i - i] = r_mul[r_i - i + 1] * nums[r_i - i + 1]
		ret = []
		for i in range(len_nums):
			ret.append(l_mul[i] * r_mul[i])
		return ret


		
sol = Solution()

print(sol.productExceptSelf([1,2,3,4])) # [24,12,8,6]
