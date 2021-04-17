# 0. 날짜 & 시도 횟수
# 2021.01.25(월요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import *
from collections import *
import heapq
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		dic = defaultdict(int)
		ret = []
		heap = []
		for num in nums:
			dic[num] += 1
		for key, val in dic.items():
			heapq.heappush(heap, (-val,val, key))

		for _ in range(k):
			ret.append(heapq.heappop(heap)[2])
		return ret







sol = Solution()
print(sol.topKFrequent([1,1,1,2,2,3], 2)) # 3
print(sol.topKFrequent([1,2], 2)) # 3
print(sol.topKFrequent([1], 1)) # 3
