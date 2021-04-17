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
		used = {}
		max_length = start = 0
		for index, char in enumerate(s):
			if char in used and start <= used[char]:
				start =used[char] + 1
			else:
				max_length = max(max_length, index - start + 1)
			used[char] = index
		return max_length








sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb" )) # 3
print(sol.lengthOfLongestSubstring("bbbbb")) # 1
print(sol.lengthOfLongestSubstring("pwwkew")) # 3
print(sol.lengthOfLongestSubstring("")) # 0
