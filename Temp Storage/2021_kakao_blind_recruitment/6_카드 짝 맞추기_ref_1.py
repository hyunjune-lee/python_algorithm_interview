# 완전 탐색(Exhaustive Search, Brute Force), 순열(Permutation)
# 2차원 배열의 너비우선탐색(BFS)
# 참고 https://www.youtube.com/watch?v=Q4bTSdi1psw&t=908s&ab_channel=ezsw
from collections import deque
import math

Board = []
all_card = {}
all_removed = 1
min_cnt = math.inf
D = ((-1, 0), (1, 0), (0, -1), (0, 1))


def bfs(removed, src, dst):
    visited = [[False for _ in range(4)] for _ in range(4)]
    q = deque([src])
    while q:
        cur = q.popleft()
        if cur[0] == dst[0] and cur[1] == dst[1]:
            return cur[2]

        for i in range(4):
            ny = cur[0] + D[i][0]
            nx = cur[1] + D[i][1]
            if ny < 0 or ny > 3 or nx < 0 or nx > 3:
                continue
            if not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, cur[2] + 1))

            for j in range(2):
                # 더 진행하다가 카드를 만난 경우
                if (removed & 1 << Board[ny][nx]) == 0:
                    break
                if ny + D[i][0] < 0 or ny + D[i][0] > 3 or nx + D[i][1] < 0 or nx + D[i][1] > 3:
                    break
                ny += D[i][0]
                nx += D[i][1]
            if not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((ny, nx, cur[2] + 1))

    return math.inf  # 혹시 에러시


def permutate(op_cnt, removed, cursor):
    global min_cnt

    # 가자치기
    if op_cnt >= min_cnt:
        return

    if removed == all_removed:
        min_cnt = min(min_cnt, op_cnt)
        return

    for num, card in all_card.items():
        if removed & 1 << num:
            continue

        one = bfs(removed, cursor, card[0]) + bfs(removed, card[0], card[1]) + 2
        two = bfs(removed, cursor, card[1]) + bfs(removed, card[1], card[0]) + 2

        permutate(op_cnt + one, removed | 1 << num, card[1])
        permutate(op_cnt + two, removed | 1 << num, card[0])


def solution(board, r, c):
    global Board, all_card, all_removed
    Board = board
    # 보드를 돌면서 같은짝의 카드들을 모아둔다.
    for y in range(4):
        for x in range(4):
            num = Board[y][x]
            if num:
                all_removed |= 1 << num  # 숫자만큼 미뤄서
                if num in all_card:
                    all_card[num].append((y, x, 0))
                else:
                    all_card[num] = [(y, x, 0)]

    permutate(0, 1, (r, c, 0))
    return min_cnt


print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
