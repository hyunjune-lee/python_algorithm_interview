from collections import defaultdict

# 단어가 하나만 다른지 체크하는 함수 따로
def is_one_char_diff(s1, s2):
	diff = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			diff += 1
		if diff == 2:
			return False
	if diff == 1:
		return True
	else:
		return False

def make_graph(words):
	graph = defaultdict(list)
	for i in range(len(words) - 1):
		for j in range(i + 1, len(words)):
			s1 = words[i]
			s2 = words[j]
			if is_one_char_diff(s1, s2):
				graph[s1].append(s2)
				graph[s2].append(s1)
	return graph


def solution(begin, target, words):
	# [예외처리] 먼저 배열에 targer이 없으면 컷
	if target not in words:
		return 0
	words += [begin]
	graph = make_graph(words)
	# 최소 단계 임으로 BFS
	visit = list()
	q = list()
	q.append((begin, 0))
	while q:
		node, path_count = q.pop(0)
		if node == target:
			return path_count
		for next in graph[node]:
			if next not in visit:
				visit.append(next)
				q.append((next, path_count + 1))

	return 0

print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log"]))
