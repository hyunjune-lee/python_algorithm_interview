# 실수한거
# [block_check 함수에서 체크 못한 조건 때문에 인덱스 에러]
#   범위 나갈 때도 false, 범위 안이라도 # 이면 False해줘야 하는데
#   범위 안에 # 인 경우만 False를 해주었다.


def find_first_open_board(board, H, W):
    for y in range(H):
        for x in range(W):
            if board[y][x] == ".":
                return (y, x)
    return (-1, -1)


def count_open_board(board):
    count = 0
    for line in board:
        for x in line:
            if x == ".":
                count += 1
    return count


def block_check(y, x, board, block, H, W):
    for dy, dx in block:
        ny = y + dy
        nx = x + dx
        if not (0 <= ny < H and 0 <= nx < W):
            return False
        if board[ny][nx] == "#":
            return False
    return True


def block_set(y, x, board, block, c):
    for dy, dx in block:
        board[y + dy][x + dx] = c


def board_cover(board, H, W, blocks):
    sy, sx = find_first_open_board(board, H, W)
    if sx == -1:
        return 1
    ret = 0
    for block in blocks:
        if block_check(sy, sx, board, block, H, W):
            block_set(sy, sx, board, block, "#")
            ret += board_cover(board, H, W, blocks)
            block_set(sy, sx, board, block, ".")

    return ret


T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    board = [list(input()) for row in range(H)]
    blocks = [[[0, 0], [1, 0], [1, -1]], [[0, 0], [1, 0], [1, 1]], [[0, 0], [1, 0], [0, 1]], [[0, 0], [0, 1], [1, 1]]]
    if count_open_board(board) % 3 == 0:
        print(board_cover(board, H, W, blocks))
    else:
        print(0)
