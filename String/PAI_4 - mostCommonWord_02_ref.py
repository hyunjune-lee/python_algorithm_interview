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
		words = [word for word in re.sub(r"[^\w]", ' ', paragraph)
			.lower().split()
				if word not in banned]

		counts = Counter(words)
		return counts.most_common(1)[0][0]






sol = Solution()

# while(True):
	# s = list(input())

print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
