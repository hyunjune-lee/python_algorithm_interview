# for 문으로 짜면 문제가 지나쳐버린다는 것 => 지나치지 않게하면 for문으로 해도 괜찮음

block_type_list = [
    [(0, 0), (1, 0), (0, 1)],
    [(0, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, -1)],
]


def block_check(block_type, y, x):
    for dy, dx in block_type_list[block_type]:
        my = dy + y
        mx = dx + x
        if not (0 <= my < h and 0 <= mx < w and board[my][mx] == "."):
            return False
    return True


def blcok_paint_or_erase(block_type, paint, y, x):
    for dy, dx in block_type_list[block_type]:
        my = dy + y
        mx = dx + x
        if paint:
            board[my][mx] = "o"
        else:
            board[my][mx] = "."


def cover():
    y = -1
    x = -1
    for i in range(h):
        for j in range(w):
            if board[i][j] == ".":
                y = i
                x = j
                break
        if y != -1:
            break
    if y == -1:
        return 1

    ret = 0
    for block_type in range(len(block_type_list)):
        if block_check(block_type, y, x):
            blcok_paint_or_erase(block_type, True, y, x)
            ret += cover()
            blcok_paint_or_erase(block_type, False, y, x)
    return ret


C = int(input())

for _ in range(C):
    h, w = map(int, input().split())
    board = []
    for y in range(h):
        board.append(list(input()))
    white_count = 0
    for line in board:
        for c in line:
            if c == ".":
                white_count += 1
    ret = 0
    if white_count % 3 == 0:
        block_max = white_count / 3
        ret = cover()
    print(ret)
