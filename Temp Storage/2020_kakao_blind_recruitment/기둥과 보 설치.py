def bo_condition_check(y, x, n, is_del):
    if is_del:
        if not bo_board[y][x]:
            return True
    # 보의 왼쪽이나 오른쪽이 기둥이거나 양쪽이 보여야 한다.
    if y - 1 >= 0 and (col_board[y - 1][x] or (x + 1 <= n and col_board[y - 1][x + 1])):
        return True
    elif x - 1 >= 0 and bo_board[y][x - 1] and x + 1 <= n and bo_board[y][x + 1]:
        return True
    return False


def col_condition_check(y, x, is_del):
    if is_del:
        if not col_board[y][x]:
            return True

    # 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다
    if y == 0:
        return True
    elif bo_board[y][x] or bo_board[y][x - 1]:
        return True
    elif y - 1 >= 0 and col_board[y - 1][x]:
        return True
    return False


bo_board = []
col_board = []


def solution(n, build_frame):
    global bo_board
    global col_board
    bo_board = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    col_board = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    for build in build_frame:
        x, y, a, b = build
        # 설치
        if b == 1:
            if a == 1:  # 보
                if bo_condition_check(y, x, n, False):
                    bo_board[y][x] = True
            else:  # 기둥
                if col_condition_check(y, x, False):
                    col_board[y][x] = True
        else:  # 삭제
            if a == 1:  # 보
                # 보를 일단 삭제하고
                bo_board[y][x] = False
                # 삭제하는 보의 양쪽에 보나, 기둥이 존재하면 조건에
                if not (
                    bo_condition_check(y, x - 1, n, True)
                    and bo_condition_check(y, x + 1, n, True)
                    and col_condition_check(y, x, True)
                    and col_condition_check(y, x + 1, True)
                ):
                    bo_board[y][x] = True
            else:  # 기둥
                # 기둥을 일단 삭제하고
                col_board[y][x] = False
                # 삭제하는 기둥의 위쪽에 연결된 보, 기둥의 조건 체크
                if not (
                    bo_condition_check(y + 1, x - 1, n, True)
                    and bo_condition_check(y + 1, x, n, True)
                    and col_condition_check(y + 1, x, True)
                ):
                    col_board[y][x] = True
    # 최종 구조물 반환
    res = []
    for x in range(n + 1):
        for y in range(n + 1):
            if col_board[y][x]:
                res.append([x, y, 0])
            if bo_board[y][x]:
                res.append([x, y, 1])
    return res



print(
    solution(
        5,
        [
            [1, 0, 0, 1],
            [1, 1, 1, 1],
            [2, 1, 0, 1],
            [2, 2, 1, 1],
            [5, 0, 0, 1],
            [5, 1, 0, 1],
            [4, 2, 1, 1],
            [3, 2, 1, 1],
        ],
    )
)
print(
    solution(
        5,
        [
            [0, 0, 0, 1],
            [2, 0, 0, 1],
            [4, 0, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [2, 1, 1, 1],
            [3, 1, 1, 1],
            [2, 0, 0, 0],
            [1, 1, 1, 0],
            [2, 2, 0, 1],
        ],
    )
)
