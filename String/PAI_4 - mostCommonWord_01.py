import re
from typing import List


class Solution:
	def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
		paragraph = paragraph.lower()
		paragraph = re.sub("[^ a-z]", " ", paragraph)
		dic = dict()
		for word in paragraph.split():
			if word in banned:
				continue
			if word not in dic:
				dic[word] = 1
			else:
				dic[word] += 1
		return str(max(dic.keys(), key = lambda x: dic[x]))



sol = Solution()

# while(True):
	# s = list(input())

print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))
