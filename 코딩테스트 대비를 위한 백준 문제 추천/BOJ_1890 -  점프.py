# [0. 날짜]
# 2021.08.01(일요일)
# 문제 유형: dp
# 걸린 시간: 12
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 가는 방향이 고정되어있으므로 맨위쪽위부터 오른쪽으로,
# 그리고 아래 줄 이렇게 진행해서 진행 경로의 수가 적힌 dp_board를 만나면
# 해당 경로에서 그 숫자만큼 오른쪽, 아래에 dp_board 에 현재 적힌 경로의 수 만큼 더해준다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution():
    for y in range(N):
        for x in range(N):
            if dp_board[y][x] and board[y][x]:
                jump_dist = board[y][x]
                # 오른쪽
                if x + jump_dist < N:
                    dp_board[y][x + jump_dist] += dp_board[y][x]
                # 아래쪽
                if y + jump_dist < N:
                    dp_board[y + jump_dist][x] += dp_board[y][x]
    return dp_board[N - 1][N - 1]


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

dp_board = [[0 for _ in range(N)] for _ in range(N)]
dp_board[0][0] = 1
print(solution())
