# [0. 날짜]
# 2021.09.27(월요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# dfs로 탐색하는데 두 가지 경우를 생각해야된다.
# 1. 탐색하는 해당 노드가 가장 긴 경로의 가운데 노드인 경우
# => 자신과 연결된 자식 트리 중에서 가장 긴 경로 2개를 골라서 체크해본다.
# 2. 자식이 1개면 그 값을 리턴한다.
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기] 
from collections import defaultdict


V = int(input())
graph = defaultdict(list)
for _ in range(V):
    infos = list(map(int, input().split()))
    node = infos[0]
    infos =  infos[1:-1]
    for i in range(0, len(infos), 2):
        graph[node].append((infos[i] , infos[i + 1]))
    
max_value = -1
visited = [False for _ in range(V + 1)]
visited[1] = True
def dfs(node):
    
    ret= []
    for next_node, w in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            ret.append(w + dfs(next_node))
    # print(ret)
    if len(ret) >= 2:
        global max_value
        ret = sorted(ret, reverse=True)[:2]
        if max_value < sum(ret) :
            max_value  = sum(ret)
    if ret:
        return max(ret)
    else:
        return 0

            
res = dfs(1)
if res > max_value:
    max_value = res
print(max_value)
    
    

