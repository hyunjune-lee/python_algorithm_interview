# 0. 날짜(시도 횟수)
# 2021.01.
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#
# 0. 날짜(시도 횟수)
# 2021.01.11(1)
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 양쪽에서 최대높이를 향해가면서 현재의 최대 높이를 계속 더해간다
# 그리고 이게 최대 불륨이고 여기서 벽 부분을 빼서 물의 공간을 구한다.
# (벽은 sum을 통해 간단히 구할 수 있다.)
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# 양쪽에서 최대높이를 향해 진행하는 것
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import List
class Solution:
	def trap(self, height: List[int]) -> int:
		if len(height) == 0:
			return 0
		max_idx = height.index(max(height))
		all_space = 0
		now_max_height = 0
		for left in range(0, max_idx):
			now_max_height = max(height[left], now_max_height)
			all_space += now_max_height
		now_max_height = 0
		for right in range(len(height) - 1, max_idx -1, -1):
			now_max_height = max(height[right], now_max_height)
			all_space += now_max_height
		return all_space - sum(height)








sol = Solution()
print(sol.trap([])) # 9

print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
print(sol.trap([4,2,0,3,2,5])) # 9
