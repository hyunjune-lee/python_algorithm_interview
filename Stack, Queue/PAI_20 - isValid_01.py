# 0. 날짜 & 시도 횟수
# 2021.01.22(금요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

class Solution:
	def isValid(self, s: str) -> bool:
		stack = []
		for c in s:
			if c == ')':
				if len(stack) == 0 or '(' != stack.pop():
					return False
			elif c == '}':
				if len(stack) == 0 or '{' != stack.pop():
					return False
			elif c == ']':
				if len(stack) == 0 or '[' != stack.pop():
					return False
			else:
				stack.append(c)
		if len(stack) != 0:
			return False
		return True

sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
