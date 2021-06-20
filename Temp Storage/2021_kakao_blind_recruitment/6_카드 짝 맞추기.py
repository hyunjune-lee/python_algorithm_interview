import collections
from itertools import permutations
import copy
from collections import deque


def ctrl_move(board, y, x, dy, dx):
    # ctrl 하기전에 이미 1번 간건 있다..
    # 그래서 2~3번간것만 체크(맨 끝에서 출발해도 최대 3번까지만 이동가능하다)
    for d in range(2, 4):
        ny = y + dy * d
        nx = x + dx * d
        last = 1
        if 4 > ny >= 0 and 4 > nx >= 0:
            last = d
            if board[ny][nx]:
                return (ny, nx)
        return (ny := y + dy * last, nx := x + dx * last)


def move_by_bfs(board, start_loc, end_loc):
    q = deque([start_loc])
    move_cnt = 0
    while q:
        cur_loc = q.popleft()
        if cur_loc == end_loc:
            return move_cnt

        y, x = cur_loc
        for dy, dx in [(+1, 0), (-1, 0), (0, +1), (0, -1)]:
            ny = y + dy
            nx = x + dx
            if 4 > ny >= 0 and 4 > nx >= 0:
                q.append((ny, nx))
                q.append(ctrl_move(board, ny, nx, dy, dx))


def solution(board, r, c):
    loc = {k: [] for k in range(1, 7)}
    for y in range(4):
        for x in range(4):
            if num := board[y][x]:
                loc[num].append((y, x))
    for p in permutations(filter(lambda v: v, loc.values())):
        start_loc = [(r, c)]
        case_board = copy.deepcopy(board)
        for a_loc, b_loc in p:
            move_by_bfs(case_board, start_loc, a_loc) + move_by_bfs(case_board, a_loc, b_loc)


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
