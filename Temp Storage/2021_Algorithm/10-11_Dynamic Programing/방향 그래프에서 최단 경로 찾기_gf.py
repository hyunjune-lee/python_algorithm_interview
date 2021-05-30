def floyd(W):
    # D = W
    # 임의로 강의자료 32p에 있는 예제의 W를 가져옴
    D = [
        [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), float("inf")],
        [float("inf"), 0, 1, float("inf"), 1, 5],
        [float("inf"), 9, 0, 3, 2, float("inf")],
        [float("inf"), float("inf"), float("inf"), 0, 4, float("inf")],
        [float("inf"), float("inf"), float("inf"), 2, 0, 3],
        [float("inf"), 3, float("inf"), float("inf"), float("inf"), 0],
    ]
    table = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    table[i][j] = k  # i => j로 갈 때 k를 경유한다.

    for i in range(1, n + 1):
        if D[i][i] < 0:
            return [-1]

    # ========================================
    result_path = print_path(table, 4, 1, [])
    print("result_path:", result_path)
    # ========================================

    return D


# ========== 경로 출력하는 것 =============
def print_path(table, start, end, result):
    if table[start][end] == 0:
        return [start, end]
    mid = table[start][end]
    left = print_path(table, start, mid, result)
    right = print_path(table, mid, end, result)
    return left + right


# ========================================


def make_graph(arr, n):
    graph = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        graph[i][i] = 0
    for i in range(0, len(arr), 3):
        graph[arr[i] + 1][arr[i + 1] + 1] = arr[i + 2]
    return graph


def find_path(W):
    if W == [-1]:
        print(-1)
        return
    max_dist = -float("inf")
    start_node, end_node = 0, 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if max_dist < W[i][j] and W[i][j] != float("inf"):
                max_dist = W[i][j]
                start_node, end_node = i - 1, j - 1

    # 정답 출력
    print(start_node, end_node, max_dist)


# for _ in range(int(input())):
#     n, e = map(int, input().split())
#     arr = list(map(int, input().split()))
#     graph = make_graph(arr, n)
#     W = floyd(graph)
#     find_path(W)

# ======== 경로 출력 테스트 ==========
n = 5
floyd([])
