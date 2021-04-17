# 0. 날짜 & 시도 횟수
# 2021.01.15(금요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 짝수번째의 합이 정답이다.
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import *
from collections import *

class Solution:
	def arrayPairSum(self, nums: List[int]) -> int:
		nums.sort()
		return sum(nums[::2])



sol = Solution()

print(sol.arrayPairSum([1,4,3,2])) # 4
print(sol.arrayPairSum([6,2,6,5,1,2])) # 9
