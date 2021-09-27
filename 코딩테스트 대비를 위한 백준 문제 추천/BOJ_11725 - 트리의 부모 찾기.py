# [0. 날짜]
# 2021.09.27(월요일)
# 문제 유형: bfs, dfs
# 걸린 시간: 8분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# visited를 list.append 형식으로 추가하는식으로 했더니 시간초과 나와서
# 미리 list를 만들어서 해당노드의 방문여부를 False, True로 저장하게 해서 해결
from collections import defaultdict

N = int(input())
tree = defaultdict(list)
parent_dic = dict()
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

q = [1]
visited = [False for _ in range(N + 1)]
while q:
    node = q.pop()
    for next_node in tree[node]:
        if not visited[next_node]:
            visited[next_node] = True
            parent_dic[next_node] = node
            q.append(next_node)

for i in range(2, N + 1):
    print(parent_dic[i])



