from typing import List

class Solution:
	def reverseString(self, s: List[str]) -> None:
		s.reverse()



sol = Solution()

while(True):
	s = list(input())
	print(sol.reverseString(s))
	print(s)
