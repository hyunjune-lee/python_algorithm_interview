# [0. 날짜]
# 2021.07.19(월요일)
# 문제 유형: dfs or bfs
# 걸린 시간: 15분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
# visited 넣으면 성능이 더 개선되려나..?
# 생각해보니 0으로 만든게 visited 체크랑 동일한 역할을 하네
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 1개짜리인 경우를 제대로 세지 못함..
# 전처리나 시작되는 지점에 대한 구체적으로 좀 더 생각해야돼


def dfs(y, x):
    res = 0
    for dy, dx in [(1, 0), (-1, 0), (0, -1), (0, +1)]:
        if not (0 <= (ny := dy + y) < N and 0 <= (nx := dx + x) < N):
            continue
        if board[ny][nx] == 1:
            board[ny][nx] = 0
            res += 1 + dfs(ny, nx)
    return res


def solution():
    res = []
    estate_count = 0
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                board[y][x] = 0
                estate_count += 1
                res.append(1 + dfs(y, x))
                for l in board:
                    print(l)
                print("=============")
    print(estate_count)
    for r in sorted(res):
        print(r)


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, list(input()))))
solution()
