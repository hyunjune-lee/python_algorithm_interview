from collections import deque, defaultdict

# 무방향을 방향으로 0을 기준으로
def solution(n, path, order):
    indegree = [0 for i in range(n)]
    con = defaultdict(list)
    visited = [0]
    q = deque(path)
    while q:
        u, v = q.popleft()
        if u in visited:
            indegree[v] += 1
            con[u].append(v)
            visited.append(v)
        elif v in visited:
            indegree[u] += 1
            con[v].append(u)
            visited.append(u)
    for u, v in order:
        indegree[v] += 1
        con[u].append(v)
    i = 0
    checked = []
    count = 0
    while any(indegree):
        for i in range(n):
            if i not in checked and indegree[i] == 0:
                for c in con[i]:
                    indegree[c] -= 1
                checked.append(i)
        count += 1
        if count > n:
            return False
    return True


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
print(solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]]))
print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))
