from typing import List

class Solution:
	def reverseString(self, s: List[str]) -> None:
		for i in range(len(s)//2):
			s[i], s[len(s) - 1 -i] = s[len(s) - 1 -i], s[i]



sol = Solution()

while(True):
	s = input()
	print(sol.reverseString(s))
	print(s)
