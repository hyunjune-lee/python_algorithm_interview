from typing import List

class Solution:
	def reverseString(self, s: List[str]) -> None:
		new_s = s[::-1]
		print(new_s)
		s = new_s



sol = Solution()

while(True):
	s = input()
	print(sol.reverseString(s))
	print(s)
