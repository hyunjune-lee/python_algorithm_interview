# 0. 날짜 & 시도 횟수
# 2021.01.15(금요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# 결국은 자신을 제외한 좌측의 곱과 우측의 곱을 곱한 것을 알아야하는데
# 이때 좌측에서의 곱을 한번 구하고 O(n)
# 우측에서의 곱을 구하고 O(n)
# 그 뒤에 진행하면서 좌측과 우측의 곱을 구해준다 O(n)
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import *
from collections import *

class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		left_mul = [1 for _ in nums]
		right_mul = [1 for _ in nums]
		ret = [1 for _ in nums]
		for i,v in enumerate(nums[:-1]):
			left_mul[i+1] *= left_mul[i] * v
		for i,v in enumerate(nums[::-1][:-1]):
			right_mul[i+1] *= right_mul[i] * v
		right_mul = right_mul[::-1]
		for i,left in enumerate(left_mul):
			ret[i] = left * right_mul[i]
		return ret


sol = Solution()

print(sol.productExceptSelf([1,2,3,4])) # [24,12,8,6]
