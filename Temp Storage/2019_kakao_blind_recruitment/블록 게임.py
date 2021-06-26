# [0. 날짜]
# 2021.06.25(금요일)
# 문제 유형:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 1. 일단 보드를 돌면서 각 번호에 맞는 좌표들을 저장하고
# 2. 이 좌표에 y 최소 최대, x 최소, 최대, 를 통해
#    해당 블록의 구역 및 빈공간을 체크
# 3. 해당 블록에 맞는 빈공간을 각 블록에 따라 저장6
# 4. 위에서부터 해당 빈공간까지 장애물이 없으면 해당 블록을 삭제
# 5. 삭제되는게 없을 때까지 반복#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. 개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# is_access함수에서 삭제되는 블록의 위쪽이 전부 깨끗한건 확인했지만
# 막상 삭제되는 블록 위치가 비어있는걸 확인 못 했음

from collections import defaultdict


def solution(board):
    def is_access(block_area):
        for y, x in block_area:
            for check_y in range(0, y):
                if board[check_y][x] != 0:
                    return False
            if board[y][x] != 0:
                return False
        return True

    block_area_dict = defaultdict(list)
    need_block_area_dict = {}

    N = len(board)
    for y in range(N):
        for x in range(N):
            if board[y][x] != 0:
                block_area_dict[board[y][x]].append((y, x))

    for block_id, block_area in block_area_dict.items():
        y_min = float("inf")
        x_min = float("inf")
        y_max = -1
        x_max = -1
        for y, x in block_area:
            y_min = min(y_min, y)
            y_max = max(y_max, y)
            x_min = min(x_min, x)
            x_max = max(x_max, x)
        need_block_area = []
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                if board[y][x] != block_id:
                    need_block_area.append((y, x))
        need_block_area_dict[block_id] = need_block_area
    is_del = True
    del_count = 0
    del_block_ids = []
    while is_del:
        is_del = False
        for block_id, block_area in need_block_area_dict.items():
            if block_id not in del_block_ids and is_access(block_area):
                del_block_ids.append(block_id)
                is_del = True
                del_count += 1
                for del_y, del_x in block_area_dict[block_id]:
                    board[del_y][del_x] = 0

    return del_count


print(
    solution(
        [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
            [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
            [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
            [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
            [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 5],
        ]
    )
)
