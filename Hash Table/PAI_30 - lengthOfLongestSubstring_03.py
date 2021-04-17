# 0. 날짜 & 시도 횟수
# 2021.01.28(목요일)
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
	def lengthOfLongestSubstring(self, s: str) -> int:
		start =  max_len = 0
		dic = dict()
		for i,c in enumerate(s):
			if c not in dic:
				dic[c] = i
				max_len = max(i - start + 1, max_len)
				continue
			start = dic[c] + 1 if dic[c] + 1 > start else start
			dic[c] = i
			max_len = max(i - start + 1, max_len)
		return max_len








sol = Solution()
print(sol.lengthOfLongestSubstring("abba")) # 2
print(sol.lengthOfLongestSubstring("abcabcbb" )) # 3
print(sol.lengthOfLongestSubstring("bbbbb")) # 1
print(sol.lengthOfLongestSubstring("pwwkew")) # 3
print(sol.lengthOfLongestSubstring("")) # 0
