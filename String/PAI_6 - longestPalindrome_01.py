# 0. 날짜(시도 횟수)
# 2021.01.10(1)
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 하나씩 진행하면서 홀수개 회문, 짝수개 회문 체크했다.
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

class Solution:
	def longestPalindrome(self, s: str) -> str:
		len_longest_palindrome = 0
		longest_palindrome = ""
		for i in range(len(s)):
			len_odd_palindrome = 1
			len_even_palindrome = 0
			o_left = 0
			o_right = 0
			for gap in range(1, len(s)//2 + 1):
				left = i - gap
				right = i + gap
				if 0 <= left and right < len(s):
					if s[left] == s[right]:
						o_left = left
						o_right = right
					else:
						break
			e_left = 0
			e_right = 0
			for gap in range(len(s)// 2 + 1):
				left = i - gap
				right = i + gap + 1
				if 0 <= left and right < len(s):
					if s[left] == s[right]:
						e_left = left
						e_right = right
					else:
						break

			len_odd_palindrome = o_right - o_left + 1
			len_even_palindrome = e_right - e_left + 1

			if len_longest_palindrome < max(len_odd_palindrome, len_even_palindrome):
				if len_odd_palindrome > len_even_palindrome:
					len_longest_palindrome = len_odd_palindrome
					longest_palindrome = s[o_left:o_right+1]
				else:
					len_longest_palindrome = len_even_palindrome
					longest_palindrome = s[e_left:e_right+1]
		return longest_palindrome




sol = Solution()

# while(True):
	# s = list(input())

print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
print(sol.longestPalindrome("ccc"))
print(sol.longestPalindrome("aacabdkacaa"))
