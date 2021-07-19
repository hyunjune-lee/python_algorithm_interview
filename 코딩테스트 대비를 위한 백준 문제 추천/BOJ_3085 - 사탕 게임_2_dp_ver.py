# [0. 날짜]
# 2021.07.18(일요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 각줄마다 첫번째칸을 가지고 진행을 한다.
# 같으면 연속 개수를 한개씩 증가시켜주고
# 다르면 분기가 생긴다.
# 1. 현재 연속된 블록을 계속 유지하기 위해 양쪽의 같은 칸이 있는지 확인한다.
# 있다면 1번만 그 칸을 넘겨서 계속 진행한다.
# solution(y, x, seq_count, left_chance)
# 2. 다른 새로운 블록으로 거기서 시작한다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 인접한 줄에서 바꾸는건 생각했는데, 한 줄내에서 바꾸는 경우를 생각X


def find_longest_seq_x(board, y, x, before_block, seq_count, left_chance):
    if x >= N:
        return seq_count
    cur_block = board[y][x]
    res = seq_count
    # 처음이라면
    if before_block == cur_block:
        res = max(res, find_longest_seq_x(board, y, x + 1, cur_block, seq_count + 1, left_chance))
    else:  # 다르다면
        res = max(res, seq_count)
        if left_chance:
            for dy in (-1, 1):
                ny = y + dy
                if ny < 0 or ny >= N:
                    continue
                new_cur_block = board[ny][x]
                if before_block == (new_cur_block):
                    res = max(res, find_longest_seq_x(board, y, x + 1, new_cur_block, seq_count + 1, 0))
                else:
                    res = max(res, find_longest_seq_x(board, y, x + 1, new_cur_block, 1, 0))
            if x + 1 < N:
                if before_block == board[y][x + 1]:
                    res = max(res, seq_count + 1)
        res = max(res, find_longest_seq_x(board, y, x + 1, cur_block, 1, left_chance))
    return res


def solution(board):
    max_res = 0
    for y in range(N):
        res = find_longest_seq_x(board, y, 0, None, 0, 1)
        # print(res)
        max_res = max(max_res, res)
    return max_res


N = int(input())
board_rotate = [["X" for _ in range(N)] for _ in range(N)]
board = []
for y in range(N):
    line = input()
    board.append(line)
    for x, c in enumerate(line):
        board_rotate[x][N - 1 - y] = c

print(max(solution(board), solution(board_rotate)))
