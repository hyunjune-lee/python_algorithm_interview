# 0. 날짜 & 시도 횟수
# 2021.01.29(금요일)
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
	def letterCombinations(self, digits: str) -> List[str]:
		def dfs(nums ,s):
			if nums == "":
				ret.append(s)
				return
			for c in phone[nums[0]]:
				dfs(nums[1:], s + c)

		phone = {
			"2" : "abc",
			"3" : "def",
			"4" : "ghi",
			"5" : "jkl",
			"6" : "mno",
			"7" : "pqrs",
			"8" : "tuv",
			"9" : "wxyz"
		}
		if not digits:
			return []
		ret = []
		dfs(digits, "")
		return ret









sol = Solution()

print(sol.letterCombinations("23")) # ["ad","ae","af","bd","be","bf","cd","ce","cf"]

print(sol.letterCombinations("")) # []

print(sol.letterCombinations("2")) #  ["a","b","c"]
