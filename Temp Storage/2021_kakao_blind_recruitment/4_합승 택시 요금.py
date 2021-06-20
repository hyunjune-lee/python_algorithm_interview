# 플로이드 알고리즘으로 모든 노드간의 최소를 구함
# 그래서 모든 노드와 a,b노드간의 거리의 합이 최소가 되는 노드를 찾는다.
# 이때 start node에서 해당 노드까지의 거리를 더해서 최소를 찾아본다.


def solution(n, s, a, b, fares):
    board = [[float("inf") if y != x else 0 for x in range(n)] for y in range(n)]
    for c, d, f in fares:
        board[c - 1][d - 1] = board[d - 1][c - 1] = f

    # <floyd>
    for k in range(n):
        for y in range(n):
            for x in range(n):
                # [tip] min으로 하는 것보다 if 문으로 하는게 속도 훨씬 빠름
                if board[y][x] > board[y][k] + board[k][x]:
                    board[y][x] = board[y][k] + board[k][x]
    min_fare = float("inf")
    # 모든 노드와 A,B 노드 간의 최소거리의 합 + start부터 그 노드까지의 최소거리
    for stopover in range(n):
        fare_from_stopover = board[a - 1][stopover] + board[b - 1][stopover]
        fare_to_stopover = board[s - 1][stopover]
        min_fare = min(min_fare, fare_from_stopover + fare_to_stopover)
    return min_fare


print(
    solution(
        6,
        4,
        6,
        2,
        [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]],
    )
)
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
