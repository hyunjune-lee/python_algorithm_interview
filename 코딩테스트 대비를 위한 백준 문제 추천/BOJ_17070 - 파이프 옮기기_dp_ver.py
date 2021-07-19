# [0. 날짜]
# 2021.07.19(월요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# q를 이용한다.
# q에서 나온 상태가 가로면 (오른쪽, 가로), (오른쪽 아래 좌표,  대각선) 이렇게 q에 넣는다.
# 하지만 이때 움직이려는 좌표가 벽이면 q에 넣지 않는다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 파이프가.. 오는 순서에 따라 q를 통해서하면 dp가 적용이 안될거라 생각했는데
# 배열을 위에서부터 차례대로 따라가면 dp가 적용이된다...ㅠ
# 방향성이 정해진 것을 보고 바로 dp를 생각해볼껄..


def solution():
    dp_board[0][1][0] = 1  # 0, 1 위치에 row 상태인 경우 1개 존재
    for y in range(N):
        for x in range(1, N):
            for state, state_count in enumerate(dp_board[y][x]):
                if state == 0:
                    next_move_n_state = [(0, 1, 0), (1, 1, 2)]
                elif state == 1:
                    next_move_n_state = [(1, 0, 1), (1, 1, 2)]
                elif state == 2:
                    next_move_n_state = [(0, 1, 0), (1, 0, 1), (1, 1, 2)]
                for dy, dx, next_state in next_move_n_state:
                    ny, nx = y + dy, x + dx
                    if not (0 <= ny < N and 0 <= nx < N) or board[ny][nx] == 1:  # 벽이라면
                        continue
                    if next_state == 2:
                        if board[y + 1][x] == 1 or board[y][x + 1] == 1:
                            continue
                    dp_board[ny][nx][next_state] += state_count
    return sum(dp_board[N - 1][N - 1])


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp_board = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]

print(solution())
