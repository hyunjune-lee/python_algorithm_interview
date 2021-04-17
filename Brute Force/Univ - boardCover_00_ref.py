def solution():
    answer = 0

    # 예외 처리 해주기
    if white_spaces % 3 != 0:
        return 0

    blocks = white_spaces // 3  # 필요한 블록(3개짜리 칸이 1개의 블록) 개수

    def board_cover(cur_r, cur_c, blocks): # dfs
        global result

        print("====================")  # 디버깅 출력 부분
        print("cur_r, cur_c, blocks:", "(", cur_r, ",", cur_c, ")", blocks)
        for ss in board:
            print(ss)

        # 종료 부분
        if blocks == 0:
            result += 1
            return

        # 조사 부분
        for r in range(row):
            for c in range(col):
                if board[r][c] == "X":
                    if r + 1 < row and c + 1 < col:
                        if board[r + 1][c] == "X" and board[r][c + 1] == "X":  #     r
                            change_to_black(r, c, r + 1, c, r, c + 1)
                            board_cover(r, c + 1, blocks - 1)
                            change_to_white(r, c, r + 1, c, r, c + 1)

                        if board[r + 1][c] == "X" and board[r + 1][c + 1] == "X":  # ㄴ
                            change_to_black(r, c, r + 1, c, r + 1, c + 1)
                            board_cover(r, c + 1, blocks - 1)
                            change_to_white(r, c, r + 1, c, r + 1, c + 1)

                        if board[r][c + 1] == "X" and board[r + 1][c + 1] == "X":  # ㄱ
                            change_to_black(r, c, r, c + 1, r + 1, c + 1)
                            board_cover(r, c + 1, blocks - 1)
                            change_to_white(r, c, r, c + 1, r + 1, c + 1)

                    if c + 1 >= 0 and r + 1 < row:
                        if board[r + 1][c] == "X" and board[r + 1][c - 1] == "X":  # ㅢ
                            change_to_black(r, c, r + 1, c, r + 1, c - 1)
                            board_cover(r, c + 1, blocks - 1)
                            change_to_white(r, c, r + 1, c, r + 1, c - 1)

                    # 첫번째 "."를 지났는데 채워지지 않았으면 종료?
                    if r >= f_row and c >= f_col and board[f_row][f_col] == "X":
                        return

    def change_to_black(i1, j1, i2, j2, i3, j3):
        board[i1][j1] = "O"
        board[i2][j2] = "O"
        board[i3][j3] = "O"

    def change_to_white(i1, j1, i2, j2, i3, j3):
        board[i1][j1] = "X"
        board[i2][j2] = "X"
        board[i3][j3] = "X"

    board_cover(0, 0, blocks)


def find_first_white():
    for i in range(row):
        for j in range(col):
            if board[i][j] == "X":
                return i, j


# row, col = map(int, input().split())
# row, col = 8, 10
row, col = 3, 7
b = ["OXXXXXO", "OXXXXXO", "OOXXOOO"]
# row, col = 3, 6
# b = ["#..###", "#....#", "##...#"]
white_spaces = 0
result = 0
# b = [
#     "##########",
#     "#........#",
#     "#........#",
#     "#........#",
#     "#........#",
#     "#........#",
#     "#........#",
#     "##########",
# ]
board = []
for x in b:
    board.append(list(x))

for i in range(row):
    for x in b[i]:
        if x == "X":
            white_spaces += 1
f_row, f_col = find_first_white()

solution()
print(result)
