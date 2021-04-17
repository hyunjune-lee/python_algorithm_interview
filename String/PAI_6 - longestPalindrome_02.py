# 0. 날짜(시도 횟수)
# 2021.01.11(2)
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#


class Solution:
	def longestPalindrome(self, s: str) -> str:
		def ret_long_palindrome(left, right, s, first_s) -> str:
			long_pailndrom = first_s
			while(0 <= left and right < len(s)):
				if s[left] == s[right]:
					long_pailndrom = s[left:right+1]
				else:
					return long_pailndrom
				left -=1
				right +=1
			return long_pailndrom



		if len(s) < 2 or s[:] == s[::-1]:
			return s
		longest_palindrome = ""
		for i in range(len(s)):
			longest_palindrome = max(longest_palindrome,
				ret_long_palindrome(i, i+1, s, s[i]),
				ret_long_palindrome(i, i+2, s, s[i]),key= len)
		return longest_palindrome





sol = Solution()

# while(True):
	# s = list(input())

print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("ccc"))
print(sol.longestPalindrome("aacabdkacaa"))
