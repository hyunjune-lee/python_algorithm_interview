# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
# 로그들을 나눠서 리스트에 저장하고 sorted를 활용해서 문제 풀음
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# list 사용, sorted 활용
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# letter_logs = sorted(letter_logs, key= lambda log : (log.split()[1:], log.split()[0]))
# 여기서 원래 log.split()[1]로 했었다. 근데 식별자뒤의 문자열 전체를 기준으로 정렬해야했기 때문에
# log.split()[1:]로 했다.



from typing import List

class Solution:
	def reorderLogFiles(self, logs: List[str]) -> List[str]:
		letter_logs = []
		digit_logs = []
		for log in logs:
			if log.split()[1].isalpha():
				letter_logs.append(log)
			else:
				digit_logs.append(log)
		letter_logs = sorted(letter_logs, key= lambda log : (log.split()[1:], log.split()[0]))
		return letter_logs + digit_logs


sol = Solution()

# while(True):
	# s = list(input())

# print(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

# Expected => ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
print(sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))

# Expected => ["a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
print(sol.reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car"]))
