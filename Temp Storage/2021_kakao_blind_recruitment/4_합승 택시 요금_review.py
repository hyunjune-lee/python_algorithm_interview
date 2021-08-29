# [0. 날짜]
# 2021.08.29(일요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 각 노드간의 모든 거리를 알면
# (S -> [1~N] 까지의 합승 요금
#   + 합승 끝나는 지점에서의 A 요금 + B 요금
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# floyd 와셜 돌릴 때 루프 돌리는 index가 중요하다!!
# 처음에 3중 for문을 i j k 순으로 하고
# shortestMat[i][j] > shortestMat[i][k] + shortestMat[k][j] 이렇게 비교했는데 틀렸다.
# 그리고 고쳐서 k i j 순으로하고
# 나머지는 그대로 해서 돌렸더니 맞았다.
# i j k 순으로 할때는 최소길이가 2번 이상 갱신되는 경우가 안되서 그런거 같다.


def solution(n, s, a, b, fares):
    shortestMat = [[float("inf") if x != y else 0 for x in range(n + 1)] for y in range(n + 1)]
    for c, d, f in fares:
        shortestMat[c][d], shortestMat[d][c] = f, f
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if shortestMat[i][j] > shortestMat[i][k] + shortestMat[k][j]:
                    shortestMat[i][j] = shortestMat[i][k] + shortestMat[k][j]

    min_fare = float("inf")
    for mid in range(1, n + 1):
        min_fare = min(min_fare, shortestMat[s][mid] + shortestMat[mid][a] + shortestMat[mid][b])
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

print(solution(7, 3, 4, 1, [[5, 7, 0], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))
