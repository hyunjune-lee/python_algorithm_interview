# l_block_list = [
#     [(0, 0), (-1, 0), (-1, -1)],
#     [(0, 0), (-1, 0), (-1, 1)],
#     [(0, 0), (1, 0), (1, -1)],
#     [(0, 0), (1, 0), (1, 1)],
#     # [(0, 0), (0, 1), (-1, 1)],
#     # [(0, 0), (0, 1), (1, 1)],
#     # [(0, 0), (0, -1), (-1, -1)],
#     # [(0, 0), (0, -1), (1, -1)],
#     # [(0, 0), (1, 0), (0, -1)],
#     # [(0, 0), (1, 0), (0, 1)],
#     # [(0, 0), (-1, 0), (0, 1)],
#     # [(0, 0), (-1, 0), (0, -1)],
# ]


# def block_check(case_number, y, x):
#     flag = True
#     for dy, dx in l_block_list[case_number]:
#         my = dy + y
#         mx = dx + x
#         if not (0 <= my < h and 0 <= mx < w and board[my][mx] == "."):
#             flag = False
#     print("case_number :", case_number, " : ", flag)
#     return flag


# def blcok_paint_n_erase(case_number, paint, y, x):
#     for dy, dx in l_block_list[case_number]:
#         my = dy + y
#         mx = dx + x
#         if paint:
#             board[my][mx] = "o"
#         else:
#             board[my][mx] = "."


# def run(block_count, ny, nx):
#     print("block_count : ", block_count)
#     # print("yy", yy, "xx", xx)
#     if block_count == block_max:
#         print("solve!!!")
#         return 1
#     # if yy == h - 1 and xx == w:
#     #     return 0
#     ret = 0
#     for sy in range(h):
#         for sy in range(w):
#             if board[yy][xx] == ".":
#                 flag = False
#                 for l_block_case in range(len(l_block_list)):
#                     if block_check(l_block_case, yy, xx):
#                         flag = True
#                         blcok_paint_n_erase(l_block_case, True, yy, xx)

#                         print("y :", yy, "x: ", xx, "case :", l_block_case)
#                         for line in board:
#                             print("".join(line))

#                         ret += run(block_count + 1, yy + (xx + 1) // w, (xx + 1) % w)
#                         # ret += run(block_count + 1)
#                         blcok_paint_n_erase(l_block_case, False, yy, xx)
#                         print("[erase]\ny :", yy, "x: ", xx, "case :", l_block_case)
#                         for line in board:
#                             print("".join(line))
#                         print("--------------------------------")

#                 if not flag:
#                     print("not flag")
#                     return ret
#     return ret


# C = int(input())

# for _ in range(C):
#     h, w = map(int, input().split())
#     board = []
#     for y in range(h):
#         board.append(list(input()))
#     white_count = 0
#     for line in board:
#         for c in line:
#             if c == ".":
#                 white_count += 1
#     ret = 0
#     if white_count % 3 == 0:
#         block_max = white_count / 3
#         print(block_max)

#         ret = run(0, 0, 0)
#         print("ret :", ret)
#         break
#     print("ret :", ret)
