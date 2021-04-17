from itertools import permutations
import math
def solution(n):
	def is_prime(can):
		if can < 2:
			return False
		for div in range(2, int(math.sqrt(can)+1)):
			if can % div == 0:
				return False
		return True

	can_set = set()
	for i in range(len(n)):
		can_set |= set(map(int, map("". join, permutations(n, i + 1))))
	answer = 0

	for can in can_set:
		if is_prime(can):
			answer += 1

	return answer


print(solution("17"))
print(solution("011"))
