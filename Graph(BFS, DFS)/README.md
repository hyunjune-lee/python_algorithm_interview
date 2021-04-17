# DFS

## 재귀 구조로 구현

1. vertex와 visited 를 매개변수로 받는다.
2. visited에 현재 v를 넣는다.
3. v와 연결된 w들을 돌면서 만약 방문을 안했다면 해당 w를 탐색한다.
4. 갱신된 visited를 반환한다.

```py
def recursive_dfs()(v, visited = []):
    visited.append(v)
    for w in graph[v]:
        if not w in visited:
            visited = recursive_dfs(w, visited)
    return visited
```

## 스택을 이용한 반복 구조로 구현

### extend ver.

```py
def iterative_dfs()(start_v):
    visited = []
    stack = [start_v]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited
```

# BFS

## 큐를 이용한 반복 구조로 구현

### extend ver.

```py
def iterative_bfs()(grahp, start_v):
    visited = []
    queue = [start_v]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited
```
