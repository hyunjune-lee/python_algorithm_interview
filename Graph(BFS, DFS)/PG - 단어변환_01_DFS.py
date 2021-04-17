from collections import defaultdict

def solution(begin, target, words):
	# [예외처리] 먼저 배열에 targer이 없으면 컷
	if target not in words:
		return 0
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
	def make_graph():
		for i in range(len(words) - 1):
			for j in range(i + 1, len(words)):
				s1 = words[i]
				s2 = words[j]
				if is_one_char_diff(s1, s2):
					graph[s1].append(s2)
					graph[s2].append(s1)

	global min_path
	min_path = 100
	def dfs(node, path_count):
		global min_path
		if node == target:
			min_path = min(min_path, path_count)
			return

		for next in graph[node]:
			if next not in visited and path_count < min_path:
				visited.append(next)
				dfs(next, path_count + 1)
				visited.pop()



	graph = defaultdict(list)
	words += [begin]
	make_graph()
	visited = []
	dfs(begin, 0)
	return min_path

print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log"]))
