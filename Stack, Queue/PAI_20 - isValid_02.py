# 0. 날짜 & 시도 횟수
# 2021.01.23(토요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		table = {
			')' : '(',
			'}' : '{',
			']' : '[',
		}
		for c in s:
			if c in table:
				if not stack or table[c] != stack[-1]:
					return False
				else:
					stack.pop()
			else:
				stack.append(c)
		if stack:
			return False
		return True



sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
