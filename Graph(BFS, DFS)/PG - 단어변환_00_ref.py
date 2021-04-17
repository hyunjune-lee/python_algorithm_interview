min_path = float("inf")
count_path = 0
visited = []


def solution(begin, target, words):
    def find(w1, w2):
        wrong = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                wrong += 1
            if wrong > 1:
                return False
        return True

    def dfs(word, arr):
        global min_path
        global count_path
        global visited
        if word in visited or not arr:
            return False

        if len(visited) > min_path:
            return False

        visited.append(word)
        count_path += 1

        if word == target:
            min_path = min(min_path, count_path)
            return True

        for i, x in enumerate(arr):
            if find(word, x):
                arr.remove(x)
                if dfs(x, arr):
                    visited.remove(x)
                    count_path -= 1
                    arr.insert(i, x)
                else:
                    break

        return min_path

    if target not in words:
        return 0
    return dfs(begin, words) - 1

print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit",	"cog",	["hot", "cog"]))
print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log"]))
