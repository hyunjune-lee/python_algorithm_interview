class Solution:
	def isPalindrome(self, s: str) -> bool:
		new_s  = ""
		for c in s:
			if(c.isalnum()):
				new_s += c
		string_len = len(new_s)
		for i in range(string_len//2):
			a = new_s[i]
			b = new_s[-(i+1)]
			if not (a.isalnum() and b.isalnum()):
				return False
			if a.isalpha() and b.isalpha():
				a = a.lower()
				b = b.lower()
			if a != b:
				return False
		return True



#==================
sol = Solution()

while(True):
	print(sol.isPalindrome(str(input())))
