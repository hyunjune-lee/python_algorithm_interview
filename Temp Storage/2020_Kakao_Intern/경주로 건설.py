from collections import deque


def solution(board):
    row = len(board)
    col = len(board[0])
    cost_board = [[[float("inf") for x in range(4)] for _ in range(col)] for i in range(row)]
    move_list = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # y, x, direction, cost, visited
    q = deque([(0, 0, -1, 0, [])])
    min_cost = float("inf")
    while q:
        y, x, direction, cost, visited = q.pop()
        if (y, x) == (row - 1, col - 1):
            min_cost = min(min_cost, cost)
            continue
        for move_direction, move in enumerate(move_list):
            dy, dx = move
            ny = y + dy
            nx = x + dx
            # 경계, 방문, 벽
            if 0 <= nx < col and 0 <= ny < row and (ny, nx) not in visited and board[ny][nx] == 0:
                # 방향이 같으면 100
                next_cost = cost
                if direction == move_direction:
                    next_cost += 100
                elif direction == -1:
                    next_cost += 100
                else:
                    next_cost += 600
                if next_cost < cost_board[ny][nx][move_direction]:
                    cost_board[ny][nx][move_direction] = next_cost
                    q.append((ny, nx, move_direction, next_cost, visited + [(ny, nx)]))
    return min_cost


print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))  # 900
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 1, 0],
            [0, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
)  # 3800
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))  # 2100
print(
    solution(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 0, 1, 0, 0, 0],
            [1, 0, 0, 1, 0, 1],
            [0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ]
    )
)  # 3200
