# 0. 날짜 & 시도 횟수
# 2021.06.24(목요일)
# 문제 유형: 완전 탐색,
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#    1. lock 보드를 key와 최소 1줄은 겹치게 확장시켜서
#    2. key를 4방향에 대한 회전을 한뒤 => 확장된 보드의 처음부터 한칸씩 움직이면서 체크해본다.
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#    1. 보드 확장
#    2. 2차원 배열 회전
#    3. 완전 탐색
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# key에서는 1이 돌기이고 lock에서는 0이 홈인데 둘다 1로 생각해서 비교할때(if extended_board[y + dy][x + dx] == square[dy][dx]) ==가 아닌 !=로 함

import copy


def rotate_square(square, rotate_count):
    l = len(square)
    square = copy.deepcopy(square)
    rotate_square = [[0 for _ in range(l)] for _ in range(l)]
    # 0, 0 -> 0, 2 / 0, 1 -> 1, 2 / 0, 2 -> 2, 2 / 1, 2 -> 2, 1
    # y는 이전의 x // x는 이전의 l - 1 - y 값
    # 1번당 90도 회전
    for _ in range(rotate_count):
        for y in range(l):
            for x in range(l):
                rotate_square[y][x] = square[x][l - 1 - y]
        square = copy.deepcopy(rotate_square)

    return rotate_square


def solution(key, lock):
    # N + (M - 1) * 2한 크기
    M = len(key)
    N = len(lock)
    board_size = N + (M - 1) * 2
    extended_board = [[2 for _ in range(board_size)] for _ in range(board_size)]
    lock_count = 0
    for y in range(N):
        for x in range(N):
            extended_board[y + M - 1][x + M - 1] = lock[y][x]
            if lock[y][x] == 0:
                lock_count += 1

    square_list = []
    square_list.append(copy.deepcopy(key))
    square_list.append(rotate_square(key, 1))
    square_list.append(rotate_square(key, 2))
    square_list.append(rotate_square(key, 3))

    # lock의 일부분만 맞아도 성공할 수 있음 => lock 개수도 세주기
    for y in range(board_size - (M - 1)):
        for x in range(board_size - (M - 1)):
            for square in square_list:
                is_open = True
                open_lock_count = 0
                for dy in range(M):
                    for dx in range(M):
                        if M - 1 <= y + dy < M - 1 + N and M - 1 <= x + dx < M - 1 + N:
                            if extended_board[y + dy][x + dx] == square[dy][dx]:
                                is_open = False
                            elif square[dy][dx] == 1:
                                open_lock_count += 1
                if is_open and open_lock_count == lock_count:
                    return True
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
