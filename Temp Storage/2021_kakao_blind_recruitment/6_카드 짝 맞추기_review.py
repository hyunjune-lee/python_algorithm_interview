# [0. 날짜]
# 2021.08.20(금요일)
# 문제 유형:
# 걸린 시간: 1시간 45분..
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 1. 해당 커서에서 모든 카드까지 도달하는 횟수와 경우의 수를 고려한다.
# 2. 카드를 고르면 한 카드를 고르면 나머지짝을 찾을 때까지의 최소 횟수를 구한다.
# 3. 해당 카드들을 제거하고 다시 1번 과정으로 돌아간다.
# 도달 횟수 구할때 ctrl 기능 구현!
# (알아야 되는 정보)
# 1. 카드가 몇번이 있는지(한번 돌면서)
# (구현할 것)
# 1. 해당 좌표에서 나머지 좌표로 도달하는 최소 횟수를 구하는 메소드
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 2차원 배열이라 deepCopy를 해줬어야 했다.
# a에서 b로 갈때와 b에서 a로 갈때 다른 경우가 존재한다.. => 시간초과 뜸
# q 돌때마다 board를 돌면서 존재하는 card 세는 로직을 not visited로 대체했던디 시간 초과 해결
from collections import defaultdict, deque
import copy


def get_min_move_count_board(board, cursor):
    min_move_count_board = [[-1 for _ in range(4)] for _ in range(4)]
    q = deque([(0, cursor)])
    while q:
        cur_move, cur_cursor = q.popleft()
        y, x = cur_cursor
        if min_move_count_board[y][x] != -1:
            continue
        min_move_count_board[y][x] = cur_move
        # 한칸 움직임
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            my, mx = y + dy, x + dx
            if 0 <= my < 4 and 0 <= mx < 4:
                q.append((cur_move + 1, (my, mx)))
        # ctrl 움직임
        for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for mul in range(1, 4):
                my, mx = y + dy * mul, x + dx * mul
                if 0 <= my < 4 and 0 <= mx < 4:
                    # 카드를 만날 때
                    if board[my][mx]:
                        q.append((cur_move + 1, (my, mx)))
                        break
                    # 끝에 도달할 때
                    if (dy != 0 and (my == 0 or my == 3)) or (dx != 0 and (mx == 0 or mx == 3)):
                        q.append((cur_move + 1, (my, mx)))
                        break
    return min_move_count_board


def solution(board, r, c):

    # 1. 해당 커서에서 모든 카드까지 도달하는 횟수와 경우의 수를 고려한다.
    cursor = (r, c)
    min_cnt = float("inf")
    num_pos_list = [[] for _ in range(7)]
    not_visited = []
    # 카드가 몇번이 있는지, 각 위치는 어디인지 기록
    for y in range(4):
        for x in range(4):
            if board[y][x]:
                num_pos_list[board[y][x]].append((y, x))
                if board[y][x] not in not_visited:
                    not_visited.append(board[y][x])
    q = deque([(board, 0, cursor, not_visited)])
    while q:
        cur_board, cur_cnt, cursor, not_visited = q.popleft()
        if not not_visited:
            min_cnt = min(min_cnt, cur_cnt)
            continue
        min_move_count_board = get_min_move_count_board(cur_board, cursor)
        for card in not_visited:
            pair_a, pair_b = num_pos_list[card]
            ay, ax = pair_a
            by, bx = pair_b
            cursor_to_a = min_move_count_board[ay][ax]
            cursor_to_b = min_move_count_board[by][bx]
            next_min_move_count_board = get_min_move_count_board(cur_board, (ay, ax))
            a_to_b = next_min_move_count_board[by][bx]
            next_min_move_count_board = get_min_move_count_board(cur_board, (by, bx))
            b_to_a = next_min_move_count_board[ay][ax]
            next_board = copy.deepcopy(cur_board)
            next_board[ay][ax] = 0
            next_board[by][bx] = 0
            next_not_visited = not_visited[:]
            next_not_visited.remove(card)

            # 현재 커서에서 a 없애고 b를 없애는 경우
            q.append((next_board, cur_cnt + cursor_to_a + a_to_b + 2, (by, bx), next_not_visited))
            # 현재 커서에서 b 없애고 a를 없애는 경우
            q.append((next_board, cur_cnt + cursor_to_b + b_to_a + 2, (ay, ax), next_not_visited))
    return min_cnt


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
