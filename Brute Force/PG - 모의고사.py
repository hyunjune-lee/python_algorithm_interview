# 14분 걸림

def solution(answers):
	answer = []
	one = [1,2,3,4,5]
	two = [2,1,2,3,2,4,2,5]
	three = [3,3,1,1,2,2,4,4,5,5]
	ans_count = [0,0,0]
	for idx, ans in enumerate(answers):
		if one[idx % len(one)] == ans:
			ans_count[0] += 1
		if two[idx % len(two)] == ans:
			ans_count[1] += 1
		if three[idx % len(three)] == ans:
			ans_count[2] += 1
	for idx, count in enumerate(ans_count):
		if count == max(ans_count):
			answer.append(idx + 1)
	return answer




print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
