# 0. 날짜 & 시도 횟수
# 2021.01.22(금요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#
from typing import List
from collections import *

class Solution:
	def removeDuplicateLetters(self, s: str) -> str:
		counter, seen, stack = Counter(s), set(), []

		for char in s:
			counter[char] -= 1
			if char in seen:
				continue
			while stack and char < stack[-1] and counter[stack[-1]] > 0:
				seen.remove(stack.pop())
			stack.append(char)
			seen.add(char)
		return ''.join(stack)



sol = Solution()
print(sol.removeDuplicateLetters("bcabc")) # abc
print(sol.removeDuplicateLetters("cbacdcbc")) # acdb
