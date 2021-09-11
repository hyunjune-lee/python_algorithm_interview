# [0. 날짜]
# 2021.09.11(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 완전탐색인가..?
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

# 무조건 이길 방법이 있는 (1, 1)로 이동합니다.
# => dfs로 경우의수를 전부 이기는 경우에 해당하는 경우의수중에 가장 긴 움직임의 횟수를 return

# 움직일 차례인데 캐릭터의 상하좌우 주변 4칸이 모두 발판이 없거나 보드 밖이라서 이동할 수 없는 경우, 해당 차례 플레이어는 패배합니다.
# 두 캐릭터가 같은 발판 위에 있을 때, 상대 플레이어의 캐릭터가 다른 발판으로 이동하여 자신의 캐릭터가 서있던 발판이 사라지게 되면 패배합니다.


def dfs(is_a_turn, aloc, bloc, board, move_cnt):
    print(is_a_turn, aloc, bloc, board, move_cnt)
    # 상하좌우
    is_avail = False
    if is_a_turn:
        loc = aloc
    else:
        loc = bloc

    # 내 차례인데 내 발판이 없다면?
    if not board[loc[0]][loc[1]]:
        if is_a_turn:
            return -1
        else:
            return 1
    ret = []
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        my, mx = loc[0] + dy, loc[1] + dx
        if 0 <= my < len(board) and 0 <= mx < len(board[0]) and board[my][mx]:
            is_avail = True
            board[loc[0]][loc[1]] = 0  # 자신의 발판 제거
            if is_a_turn:
                ret.append(dfs(0, [my, mx], bloc, board, move_cnt + 1))
            else:
                ret.append(dfs(1, aloc, [my, mx], board, move_cnt + 1))
            board[loc[0]][loc[1]] = 1
    # 이동할 수 없었던 경우
    # a 턴이면 1을 b 턴이면 0을 반환
    if not is_avail:
        if is_a_turn:
            return -1
        else:
            return 1
    # 모두 a가 이긴 경우
    print("ret", ret)
    if sum(ret) == len(ret):
        return 1
    elif sum(ret) == len(ret) * -1:  # 모두 b가 이긴 경우
        return -1
    return 0  # a가 이길수도, b가 이길수도 있던 상황


def solution(board, aloc, bloc):
    a_turn = True

    return dfs(1, aloc, bloc, board, 0)


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
# print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
# print(solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]))
# print(solution([[1]], [0, 0], [0, 0]))
