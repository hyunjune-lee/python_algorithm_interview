def find_shortest_path_by_floyd(n, mat):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if mat[i][j] > mat[i][k] + mat[k][j]:
                    mat[i][j] = mat[i][k] + mat[k][j]
                    table[i][j] = k

    for line in table:
        print(line)

    for i in range(1, n + 1):
        if mat[i][i] < 0:
            return [-1]

    longest_path = -float("inf")
    long_path_list = []
    for y in range(1, n + 1):
        for x in range(1, n + 1):
            if longest_path < mat[y][x] and mat[y][x] != float("inf"):
                longest_path = mat[y][x]
                long_path_list = []
                long_path_list.append((y - 1, x - 1, mat[y][x]))
            elif longest_path == mat[y][x]:
                long_path_list.append((y - 1, x - 1, mat[y][x]))

    return sorted(long_path_list)[0]


T = int(input())
for _ in range(T):
    N, E = map(int, input().split())
    edge_list = list(map(int, input().split()))
    mat = [[float("inf") if x != y else 0 for x in range(N + 1)] for y in range(N + 1)]
    table = [[float("inf") if x != y else 0 for x in range(N + 1)] for y in range(N + 1)]
    for idx in range(E):
        i = 3 * idx
        start_node, end_node, weight = edge_list[i], edge_list[i + 1], edge_list[i + 2]
        mat[start_node + 1][end_node + 1] = weight

    print(" ".join(map(str, find_shortest_path_by_floyd(N, mat))))
