# 0. 날짜 & 시도 횟수
# 2021.01.16(토요일)
# 시도 횟수 : 4 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# sum에 따른 적절한 인덱스 변화 및 중복된 값일시 넘어가는 스킬
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# sum < 0 일때 right -=1하고 sum > 0 일 때 left +=1 로 했다.

from typing import *
from collections import *

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		ret = []
		for i in range(len(nums) - 2):
			if 0 < i and nums[i] == nums[i-1]:
				continue
			l, r= i + 1, len(nums) - 1
			while l < r:
				sum = nums[i] + nums[l] + nums[r]
				if sum < 0:
					l += 1
					continue
				if sum > 0:
					r -= 1
					continue
				ret.append([nums[i], nums[l], nums[r]])
				while l < r and nums[l] == nums[l + 1]:
					l += 1
				while l < r and nums[r] == nums[r - 1]:
					r -= 1
				l+=1
				r-=1
			i += 1
		return ret







sol = Solution()
print(sol.threeSum([])) # []
print(sol.threeSum([0])) # []
print(sol.threeSum([0,0,0])) # [[0, 0, 0]]
print(sol.threeSum([0,0,0,0])) # [[0, 0, 0]]
print(sol.threeSum([1,-1,-1,0])) # [[-1,0,1]]




print(sol.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
