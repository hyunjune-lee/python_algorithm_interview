# 틀린 이유 union할때 무조건 이전 마감시간에 붙여야하는데
# 나는 크기에 따라서 큰쪽에 붙여주도록해서 문제가 생겼음
def find_optimal_schedule(tasks, max_d):
    parent = dict()
    size = dict()

    def make_set(node):
        parent[node] = node
        size[node] = 1

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node_v, node_u):
        root1 = find(node_v)
        root2 = find(node_u)

        parent[root2] = root1
        size[root1] += size[root2]
        size[root2] = 0

    for i in range(max_d + 1):
        make_set(i)

    tasks.sort(key=lambda x: -x[2])

    S = []
    for i in range(len(tasks)):
        id, deadline, profit = tasks[i]
        slot = find(deadline)
        if slot > 0:
            union(find(slot - 1), slot)
            S.append(id)
    S.sort()
    return S


T = int(input())
for _ in range(T):
    N = int(input())
    task_list = list(map(int, input().split()))
    tasks = []
    max_d = 0
    for i in range(len(task_list) // 2):
        tasks.append((i + 1, task_list[2 * i], task_list[2 * i + 1]))
        max_d = max(max_d, task_list[2 * i])

    print(" ".join(map(str, find_optimal_schedule(tasks, max_d))))
