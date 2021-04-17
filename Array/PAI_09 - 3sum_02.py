# 0. 날짜 & 시도 횟수
# 2021.01.14(목요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import List
from collections import  defaultdict
class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		if len(nums) < 3:
			return []
		dic  = defaultdict(int)
		for num in nums:
			dic[num] += 1
		ret = []

		for i in range(len(nums) - 1):
			for j in range(i+1, len(nums)):
				k_v =-(nums[i]+nums[j])
				if dic[k_v] >= 1:
					is_ok = True
					pre_li = sorted([nums[i],nums[j], -(nums[i]+nums[j])])
					if pre_li in ret:
						continue
					check_dic = defaultdict(int)
					for v in pre_li:
						check_dic[v] += 1
					for c in check_dic:
						if check_dic[c] > dic[c]:
							is_ok = False
					if is_ok:
						ret.append(pre_li)
		return ret







sol = Solution()
# print(sol.threeSum([])) # []
# print(sol.threeSum([0])) # []
print(sol.threeSum([0,0,0])) # []

# print(sol.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
