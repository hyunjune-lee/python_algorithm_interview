# 0. 날짜(시도 횟수)
# 2021.01.11
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 키값을 조회하는 방식을 구현해봐야겠다.
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# 처음에 가지치기를 위한 nums[i] >= target 인경우는 continue로 지나치도록 했지만
# 0,0 마이너스인 경우가 있어서 그냥 삭제했다.


from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		for i in range(len(nums) - 1):
			for j in range(i+1, len(nums)):
				if nums[i] + nums[j] == target:
					return [i,j]



sol = Solution()

print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))
print(sol.twoSum([0,4,3,0], 0))
