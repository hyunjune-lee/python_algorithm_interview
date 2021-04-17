
# 타임 에러
from typing import List
from collections import  defaultdict
class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		if len(nums) < 3:
			return []
		ret = []
		for i in range(len(nums) - 1):
			for j in range(i+1, len(nums)):
				if -(nums[i] + nums[j]) in nums[(j+1):] and sorted([nums[i],nums[j], -(nums[i]+nums[j])]) not in ret:
					ret.append(sorted([nums[i],nums[j], -(nums[i]+nums[j])]))
		return ret







sol = Solution()
print(sol.threeSum([])) # []
print(sol.threeSum([0])) # []

print(sol.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
