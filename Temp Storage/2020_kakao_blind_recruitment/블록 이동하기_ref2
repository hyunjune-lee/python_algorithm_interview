import queue

ROW = 0
COL = 1
MAX_VAL = 9876543210

def solution(board):
    answer = 0
    size = len(board)
    _board = [[1 for _ in range(size + 2)]] + [[1, *item, 1] for item in board] + [[1 for _ in range(size + 2)]]

    row_values = [[MAX_VAL for _ in range(size + 2)] for _ in range(size + 2)]
    col_values = [[MAX_VAL for _ in range(size + 2)] for _ in range(size + 2)]


    que = queue.Queue()
    que.put((1, 1, 0, ROW))

    while not que.empty():
        x, y, time, mode = que.get()
        # 가로인 경우
        if mode == ROW:
            # 벽이 있는 경우 계산을 하지 않는다.
            if _board[y][x] == 1 or _board[y][x + 1] == 1:
                continue
            # 이전에 업데이트한 값보다 작거나 같은 경우 무시한다.
            if row_values[y][x] <= time:
                continue
            row_values[y][x] = time
            # 4가지 회전에 대해서 큐에 넣는다.
            if _board[y - 1][x + 1] != 1:
                que.put((x, y - 1, time + 1, COL))
            if _board[y + 1][x + 1] != 1:
                que.put((x, y, time + 1, COL))
            if _board[y - 1][x] != 1:
                que.put((x + 1, y - 1, time + 1, COL))
            if _board[y + 1][x] != 1:
                que.put((x + 1, y, time + 1, COL))
            # 상하좌우 이동
            que.put((x, y - 1, time + 1, ROW))
            que.put((x, y + 1, time + 1, ROW))
            que.put((x + 1, y, time + 1, ROW))
            que.put((x - 1, y, time + 1, ROW))
        # 세로인 경우
        else:
            # 벽이 있는 경우 계산을 하지 않는다.
            if _board[y][x] == 1 or _board[y + 1][x] == 1:
                continue
            # 이전에 업데이트한 값보다 작거나 같은 경우 무시한다.
            if col_values[y][x] <= time:
                continue
            col_values[y][x] = time
            # 4가지 회전에 대해서 큐에 넣는다.
            if _board[y + 1][x - 1] != 1:
                que.put((x - 1, y, time + 1, ROW))
            if _board[y + 1][x + 1] != 1:
                que.put((x, y, time + 1, ROW))
            if _board[y][x - 1] != 1:
                que.put((x - 1, y + 1, time + 1, ROW))
            if _board[y][x + 1] != 1:
                que.put((x, y + 1, time + 1, ROW))
            # 상하좌우 이동
            que.put((x, y - 1, time + 1, COL))
            que.put((x, y + 1, time + 1, COL))
            que.put((x + 1, y, time + 1, COL))
            que.put((x - 1, y, time + 1, COL))

    answer = min(row_values[size][size - 1], col_values[size - 1][size])
    return answer
