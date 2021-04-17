def min_path(grid, M, N):
    go_info = [[0, 1], [1, 0]]

    q = [((0, 0), grid[0][0])]
    while q:
        coord, w = q.pop(0)
        if coord[0] == M - 1 and coord[1] == N - 1:
            ret_list.append(w)
        for dy, dx in go_info:
            ny = dy + coord[0]
            nx = dx + coord[1]
            if 0 <= ny < M and 0 <= nx < N:
                q.append(((ny, nx), w + grid[ny][nx]))


T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(M)]
    ret_list = []
    min_path(grid, M, N)
    if ret_list:
        print(min(ret_list))
