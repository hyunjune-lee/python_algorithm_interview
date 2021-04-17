# 0. 날짜 & 시도 횟수
# 2021.01.14(목요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import *
from collections import *


from typing import List
class Solution:
	def trap(self, height: List[int]) -> int:
		height_len = len(height)
		if height_len == 0:
			return 0
		top_idx = height.index(max(height))
		max_val = 0
		volume = 0
		for left_idx in range(0,top_idx):
			max_val = max(max_val, height[left_idx])
			volume += max_val
		max_val = 0
		for right_idx in range(height_len -1, top_idx-1, -1):
			max_val = max(max_val, height[right_idx])
			volume += max_val
		return volume - sum(height)




sol = Solution()
print(sol.trap([])) # 9

print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(sol.trap([4,2,0,3,2,5])) # 9
