move = [(0, 0), (0, 1), (1, 0), (1, 1)]


def check_four_blocks(y, x, board):
    if (
        board[y][x] == board[y + 1][x] == board[y][x + 1] == board[y + 1][x + 1]
        and board[y][x] != "@"
        and board[y][x] != "*"
    ):
        record = []
        for dy, dx in move:
            my = y + dy
            mx = x + dx
            record.append((my, mx))
        return record
    else:
        return None


def solution(m, n, board):
    rotate_board = []
    for i in range(n):
        rotate_row = []
        for j in range(m):
            rotate_row.append(board[j][i])
        rotate_board.append(rotate_row)
    start = True
    del_block_list = []
    del_count = 0
    while start or len(del_block_list) > 0:
        start = False
        for dy, dx in del_block_list:
            rotate_board[dy][dx] = "@"
        del_block_list = []
        for row in rotate_board:
            while "@" in row:
                row.remove("@")
                row.insert(0, "*")
                del_count += 1
        for y in range(n - 1):
            for x in range(m - 1):
                record = check_four_blocks(y, x, rotate_board)
                if record is not None:
                    del_block_list.extend(record)
    return del_count


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
