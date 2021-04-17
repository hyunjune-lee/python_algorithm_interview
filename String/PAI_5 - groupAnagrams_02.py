from typing import *
from collections import *
class Solution:
	def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
		dic = defaultdict(list)
		for s in strs:
			dic[''.join(sorted(s))].append(s)
		return dic.values()




sol = Solution()

# while(True):
	# s = list(input())

print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
