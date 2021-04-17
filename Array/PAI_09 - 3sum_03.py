# 0. 날짜 & 시도 횟수
# 2021.01.14(목요일)
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
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		left = 0
		right = len(nums) -1
		ret = []
		nums.sort()
		while left + 1 < right:
			target = -(nums[left] +nums[right])
			if target < nums[left]:
				right -=1
				continue
			if target > nums[right]:
				left +=1
				continue
			for i in range(left + 1, right):
				if nums[i] == target:
					ret.append([nums[left], nums[i],  nums[right]])
			left+=1
		return ret








sol = Solution()
# print(sol.threeSum([])) # []
# print(sol.threeSum([0])) # []
# print(sol.threeSum([0,0,0])) # []

print(sol.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
