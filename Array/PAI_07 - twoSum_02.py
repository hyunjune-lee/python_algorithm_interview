# 0. 날짜
# 2021.01.14
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# defaultdict(int) 사전에 값들과 인덱스+1한 값을 넣는다. 후에 0 이 아니면 정답을 찾은 걸로 하기 위해서
# 주어진 num을 순회하면서 target에서 뺀 값이 사전에서 0이 아니면 정답임으로 인덱스를 다시 계산해서 반환해준다.
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import List
from collections import *

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		dic = defaultdict(int)
		for i, n in enumerate(nums):
			dic[n] = i + 1
		for i, n in enumerate(nums):
			if dic[target - n] is not 0 and dic[target - n] > i+1 :
				return [i, dic[target - n] - 1]




sol = Solution()

print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))
print(sol.twoSum([3,3], 6))
print(sol.twoSum([0,4,3,0], 0))
print(sol.twoSum([2,5,5,11], 10))
