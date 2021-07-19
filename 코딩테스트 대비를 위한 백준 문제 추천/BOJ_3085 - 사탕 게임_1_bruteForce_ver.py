# [0. 날짜]
# 2021.07.19(월요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 완전 탐색으로 해볼만한 문제는.. 완전 탐색 접근을 먼저 해보자.. 겁먹지말고 냉철하게 판단하자


def find_longest_seq(board, check_y_list):
    max_seq_count = 0
    for y in check_y_list:
        if y >= N:
            continue
        seq_count = 1
        for x in range(N - 1):
            if board[y][x] == board[y][x + 1]:
                seq_count += 1
            else:
                max_seq_count = max(seq_count, max_seq_count)
                seq_count = 1
        max_seq_count = max(seq_count, max_seq_count)
    return max_seq_count


def solution(board):
    longest_seq = find_longest_seq(board, [y for y in range(0, N)])
    for y in range(N):
        for x in range(N - 1):
            board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]
            longest_seq = max(longest_seq, find_longest_seq(board, [y]))
            board[y][x], board[y][x + 1] = board[y][x + 1], board[y][x]

    for y in range(N - 1):
        for x in range(N):
            board[y + 1][x], board[y][x] = board[y][x], board[y + 1][x]
            longest_seq = max(longest_seq, find_longest_seq(board, [y, y + 1]))
            board[y + 1][x], board[y][x] = board[y][x], board[y + 1][x]
    return longest_seq


N = int(input())
board_rotate = [["X" for _ in range(N)] for _ in range(N)]
board = []
for y in range(N):
    line = input()
    board.append(list(line))
    for x, c in enumerate(line):
        board_rotate[x][N - 1 - y] = c

print(max(solution(board), solution(board_rotate)))
