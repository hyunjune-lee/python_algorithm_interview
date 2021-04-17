# 0. 날짜 & 시도 횟수
# 2021.01.22(금요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# 문제이해를 잘못함
from typing import List
from collections import *

class Solution:
	def removeDuplicateLetters(self, s: str) -> str:
		dic = dict()
		for c in "abcdefghijklmnopqrstuvwxyz":
			dic[c] = False
		for c in s:
			dic[c] = True
		s = ""
		for d in dic:
			if dic[d]:
				s += d
		return s


sol = Solution()
print(sol.removeDuplicateLetters("bcabc"))
print(sol.removeDuplicateLetters("cbacdcbc"))
