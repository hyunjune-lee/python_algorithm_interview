# 0. 날짜(시도 횟수)
# 2021.01.10(2)_ref
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from collections import *
from typing import List
class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		dic = defaultdict(list)
		for s in strs:
			dic[''.join(sorted(s))].append(s)
		return dic.values()





sol = Solution()

# while(True):
	# s = list(input())

print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
