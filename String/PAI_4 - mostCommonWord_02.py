# 0. 날짜(시도 횟수)
# 2021.01.10
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)

from collections import *
from typing import List
import re

class Solution:
	def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
		paragraph = paragraph.lower()
		paragraph = re.sub("[^0-9a-z]", " ", paragraph)
		dic = defaultdict(int)
		for word in paragraph.split():
			if word not in banned:
				dic[word] += 1
		return max(dic.items(), key = lambda word : word[1])[0]






sol = Solution()

# while(True):
	# s = list(input())

print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
