# 다익스트라

## 코드

```py
from typing import List
import heapq

def Dijkstra(self, edges: List[List[int]], start_node: int) -> int:
    dist_list = defaultdict(lambda: float("inf"))
    visited = defaultdict(lambda: False)
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
    Q = [(0, start_node)]
    while Q:
        dist, node = heapq.heappop(Q)
        if not dist_list[node]:
            dist_list[node] = dist
            visited[node] = True
            for next_node, add_dist in graph[node]:
                if not visited[next_node]:
                    delta_dist = dist + add_dist
                    heapq.heappush(Q, (delta_dist, next_node))

    return dist_list
```

```py
from collections import defaultdict
from typing import List
import heapq


def Dijkstra(self, edges: List[List[int]], start_node: int) -> int:
    graph = defaultdict(list)
    cost_list = defaultdict(lambda: float("inf"))
    visited = defaultdict(lambda: False)

    for u, v, w in edges:
        graph[u].append((v, w))

    q = [(0, S)]
    visited[0] = True
    while q:
        cost, node = heapq.heappop(q)
        visited[node] = True
        cost_list[node] = cost
        for next_node, add_cost in graph[node]:
            if not visited[next_node]:
                delta_cost = cost + add_cost
                heapq.heappush(q, (delta_cost, next_node))
    return cost_list[D]

```

## 과정

### 그래프 만들기

1. 그래프를 defaultdict(list)을 활용하여 만든다.
2. 가중치 그래프를 채운다.

### 거리 및 힙큐 초기화

1. 거리를 defaultdict(int)로 초기화
2. heapq에다가 [[(0, start_node)]] 넣기

### 다익스트라 알고리즘 부분

1. 힙큐가 빌때까지
2. 힙에서 제일짧은 거리를 가진 노드를 추출하고
3. 해당 노드가 갱신된 적이 없을 떄
   (제일 짧은 거리를 가지고 차례대로 추적하기 때문에 처음 갱신될 때가 최솟값이다)
4. 해당 노드의 거리를 갱신하고
5. 해당 노드와 연결된 노드들의 거리를 현재 거리와 더해서 다시 힙에 넣어준다.

## 주의점

heap에 넣을때는 첫번째 요소로 힙이 구성되기 때문에 앞에다가 가중치를 넣고 뒤에 도착 노드를 적어야한다.
