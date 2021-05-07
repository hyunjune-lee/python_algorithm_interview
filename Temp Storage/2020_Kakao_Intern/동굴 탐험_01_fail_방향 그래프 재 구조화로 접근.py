from collections import deque, defaultdict


# 무방향을 방향으로 0을 기준으로\
# 일단 인접 행렬을 만들고 0을 기준으로 방향성 만들기
def solution(n, path, order):
    visited = [False for _ in range(n)]
    con = defaultdict(list)

    for u, v in path:
        con[u].append(v)
        con[v].append(u)
    for u, v in order:
        con[u].append(v)
        con[v] = [u]
    print(con)
    q = [0]
    while q:
        node = q.pop()
        for next_node in con[node]:
            print(next_node)
            if not visited[next_node]:
                q.append(next_node)
        visited[node] = True
    print(visited)


# 비효율적으로 parent, con 생성
# def solution(n, path, order):
#     # indegree = [0 for i in range(n)]
#     con = defaultdict(list)
#     parent = defaultdict(list)
#     visited = [0]
#     q = deque(path)
#     while q:
#         u, v = q.popleft()
#         if u in visited:
#             # indegree[v] += 1
#             parent[v].append(u)
#             con[u].append(v)
#             visited.append(v)
#         elif v in visited:
#             # indegree[u] += 1
#             parent[u].append(v)
#             con[v].append(u)
#             visited.append(u)
#         else:
#             q.append((u, v))
#     # print(con)
#     # print(parent)
#     for u, v in order:
#         # indegree[v] += 1
#         con[parent[v][0]].remove(v)
#         con[u].append(v)
#     # print(con)
#     q = [0]
#     visited = [0]
#     while q:
#         node = q.pop()
#         for c in con[node]:
#             q.append(c)
#             visited.append(c)
#         # print(visited)
#     return len(visited) == n


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
# print(solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]]))
# print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))
