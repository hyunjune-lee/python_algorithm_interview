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

class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		max_len = 0
		len_s = len(s)
		for start in range(len_s):
			end = start + max_len
			if end > len_s:
				return max_len
			while end - start == len(set(s[start:end])):
				end += 1
			max_len = max(len(s[start:end-1]), max_len)
		return max_len








sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb" )) # 3
print(sol.lengthOfLongestSubstring("bbbbb")) # 1
print(sol.lengthOfLongestSubstring("pwwkew")) # 3
print(sol.lengthOfLongestSubstring("")) # 0
