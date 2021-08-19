# 716ms
def solution(n):
    dp_board = [[0 for _ in range(n + 1)] for _ in range(4)]
    dp_board[0][0] = 1
    for y in range(4):
        for x in range(n + 1):
            for add_num in [1, 2, 3]:
                if dp_board[y][x] and y <= add_num and x + add_num < n + 1:
                    dp_board[add_num][x + add_num] += dp_board[y][x]
    return sum([dp_board[y][n] for y in range(4)])


T = int(input())
for _ in range(T):
    n = int(input())
    print(solution(n))
