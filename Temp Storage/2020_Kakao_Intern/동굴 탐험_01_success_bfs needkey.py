from collections import deque, defaultdict


def solution(n, path, order):
    con = defaultdict(list)
    need_visit = [1 for _ in range(n)]
    key_dic = dict()
    for u, v in path:
        con[u].append(v)
        con[v].append(u)
    for u, v in order:
        key_dic[u] = v
        need_visit[v] = 3
    if need_visit[0] != 1:
        return False
    q = deque([0])
    need_visit[0] = 0
    while q:
        node = q.popleft()
        for next_node in con[node]:
            if need_visit[next_node] == 1:
                q.append(next_node)
                need_visit[next_node] = 0
                if next_node in key_dic:
                    cur_available_node = key_dic[next_node]
                    if need_visit[cur_available_node] == 2:
                        q.append(cur_available_node)
                        need_visit[cur_available_node] = 1
                    else:
                        need_visit[cur_available_node] = 1
                    del key_dic[next_node]
            elif need_visit[next_node] == 3:
                need_visit[next_node] = 2
    return sum(need_visit) == 0


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))
print(solution(9, [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]], [[4, 1], [5, 2]]))
print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[4, 1], [8, 7], [6, 5]]))
