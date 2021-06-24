# [0. 날짜]
# 2021.06.24(목요일)
# 문제 유형: 동적프로그래밍? / 가로 모드, 세로모드가 혼재한 다이나믹 프로그래밍?// dfs?
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +한번에 맞추지 못한 경우 오답 원인 적기]
#
# [4. 개선사항]
# 1. visited를 하는데 이때 y,x, (가로,세로)도
# 2. 지금 2개의 좌표에 대해서 움직이지만.. 1개의 좌표로 설정해도 상관없을듯..
# [가로 일 때]
# 상하좌우, 회전(가능 여부 체크)
# [세로 일 때]
# 상하좌우, 회전(가능 여부 체크)


def is_move(robot_loc, direction):
    if direction == "up":
        next_robot_loc = [(y - 1, x) for y, x in robot_loc]
    elif direction == "down":
        next_robot_loc = [(y + 1, x) for y, x in robot_loc]
    elif direction == "left":
        next_robot_loc = [(y, x - 1) for y, x in robot_loc]
    elif direction == "right":
        next_robot_loc = [(y, x + 1) for y, x in robot_loc]

    for my, mx in next_robot_loc:
        if not is_in_board(my, mx):
            return False
    return True


def move(robot_loc, direction):
    if direction == "up":
        next_robot_loc = [(y - 1, x) for y, x in robot_loc]
    elif direction == "down":
        next_robot_loc = [(y + 1, x) for y, x in robot_loc]
    elif direction == "left":
        next_robot_loc = [(y, x - 1) for y, x in robot_loc]
    elif direction == "right":
        next_robot_loc = [(y, x + 1) for y, x in robot_loc]

    return next_robot_loc


def is_in_board(my, mx):
    global board
    n = len(board)
    if 0 <= my < n and 0 <= mx < n and board[my][mx] != 1:
        return True
    return False


def is_rotate(robot_loc, direction_y, direction_x):
    global board
    (y1, x1), (y2, x2) = robot_loc
    if is_vertical(robot_loc):
        if direction_x == "left":
            if is_in_board(y1, x1 - 1) and is_in_board(y2, x2 - 1):
                if board[y1][x1 - 1] == 0 and board[y2][x2 - 1] == 0:
                    return True
        elif direction_x == "right":
            if is_in_board(y1, x1 + 1) and is_in_board(y2, x2 + 1):
                if board[y1][x1 + 1] == 0 and board[y2][x2 + 1] == 0:
                    return True
    else:
        if direction_y == "up":  # 위쪽이면 드론 위 2칸 모두 0이어야한다.
            if is_in_board(y1 - 1, x1) and is_in_board(y2 - 1, x2):
                if board[y1 - 1][x1] == 0 and board[y2 - 1][x2] == 0:
                    return True
        elif direction_y == "down":
            if is_in_board(y1 + 1, x1) and is_in_board(y2 + 1, x2):
                if board[y1 + 1][x1] == 0 and board[y2 + 1][x2] == 0:
                    return True

    return False


def rotate(robot_loc, direction_y, direction_x):
    global board
    (y1, x1), (y2, x2) = robot_loc

    # left면 left 날개가 회전하는거
    if is_vertical(robot_loc):
        if direction_x == "left":
            if direction_y == "up":
                next_robot_loc = [(y2, x2 - 1), (y2, x2)]
            elif direction_y == "down":
                next_robot_loc = [(y1, x1), (y1, x1 - 1)]
        if direction_x == "right":
            if direction_y == "up":
                next_robot_loc = [(y2, x2 + 1), (y2, x2)]
            elif direction_y == "down":
                next_robot_loc = [(y1, x1), (y1, x1 + 1)]
    else:
        if direction_y == "up":
            if direction_x == "left":
                next_robot_loc = [(y2 - 1, x2), (y2, x2)]
            elif direction_x == "right":
                next_robot_loc = [(y1, x1), (y1 - 1, x1)]
        elif direction_y == "down":
            if direction_x == "left":
                next_robot_loc = [(y2 + 1, x2), (y2, x2)]
            elif direction_x == "right":
                next_robot_loc = [(y1, x1), (y1 + 1, x1)]

    return next_robot_loc


def is_reach(robot_locs):
    for robot_loc in robot_locs:
        (y1, x1), (y2, x2) = robot_loc
        n = len(board)
        if (y1 == n - 1 and x1 == n - 1) or (y2 == n - 1 and x2 == n - 1):
            return True
    return False


def is_vertical(robot_loc):
    (y1, x1), (y2, x2) = robot_loc
    if y2 - y1 == -1 or y2 - y1 == +1:
        return True
    else:
        return False


def record(dp_board, robot_loc, move_cnt):
    v = 1
    if is_vertical(robot_loc):
        v = 0

    is_record = False
    for y, x in robot_loc:
        if dp_board[y][x][v] == -1:
            is_record = True
            dp_board[y][x][v] = move_cnt
    return is_record


board = []

import copy
from collections import deque


def solution(input_board):
    global board
    board = input_board
    dp_board = [[[-1, -1] for _ in range(len(board))] for _ in range(len(board))]
    robot_loc = [(0, 0), (0, 1)]

    move_cnt = 0
    q = deque([robot_loc])
    while not is_reach(q):
        robot_locs = []
        # print(q)
        while q:
            robot_locs.append(q.popleft())
        for robot_loc in robot_locs:
            if record(dp_board, robot_loc, move_cnt):
                for direction in ["down", "right", "left", "up"]:
                    if is_move(robot_loc, direction):
                        next_robot_loc = move(robot_loc, direction)
                        q.append(next_robot_loc)
                for direction_y in ["down", "up"]:
                    for direction_x in ["right", "left"]:
                        if is_rotate(robot_loc, direction_y, direction_x):
                            next_robot_loc = rotate(robot_loc, direction_y, direction_x)
                            q.append(next_robot_loc)
        # for line in dp_board:
        #     print(line)
        # print("=========")
        move_cnt += 1
    return move_cnt


print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))
