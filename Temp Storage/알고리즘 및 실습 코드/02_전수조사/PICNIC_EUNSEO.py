from collections import defaultdict


def match(pairs):
	pdict = defaultdict(list)
	i = 0
	while i + 1 < len(pairs):
		pdict[pairs[i]].append(pairs[i + 1])
		pdict[pairs[i + 1]].append(pairs[i])
		i += 2
	return pdict


def solution(num, pairs):
	pdict = match(pairs)

	print(pdict)
	def match_students(cur, left, matched):
		# print("matched", matched)
		if left == 0:
			result.append(matched)
			return

		for i in range(cur, num - 1):
			for j in range(i + 1, num):
				if j in pdict[i] and i in pdict[j] and i not in matched and j not in matched:
					match_students(i + 1, left - 2, matched + [i, j])

	match_students(0, num, [])


result = []
num = 4
pairs = [0, 1, 1, 2, 2, 3, 3, 0, 0, 2, 1, 3]
solution(num, pairs)
print(result)
result = []
num = 2
pairs = [0, 1]
solution(num, pairs)
print(result)
result = []
num = 4
pairs = [0, 1, 2, 3]
solution(num, pairs)
print(result)
