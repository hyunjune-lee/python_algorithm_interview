# [0. 날짜]
# 2021.08.07(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 행렬이 5개가 존재할때
#   A B C
# i 0 1 2
# memo[s][e] = s번째 행렬부터 e번째 행렬까지의 곱센 연산의 최솟값이라 해보자
# memo[s][e] = memo[s][i] + memo[i + 1][e] + mat[s][0]*mat[i][1] * mat[e][1]
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 앞뒤 분할
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
#    for i in range(s, e)에서 s가 아닌 s+1부터 범위를 주어서 틀렸다..
# 한끗차이를 디테일하기 봐야할거 같다.

#[memo 0기준 880ms]
def sol(s, e):
    if memo[s][e]:
        return memo[s][e]
    if e - s == 1:
        memo[s][e] = mats[s][0] * mats[s][1] * mats[e][1]
        return memo[s][e]
    if s == e:
        return 0
    ret = 0
    for i in range(s, e):
        ret = sol(s, i) + sol(i + 1, e) + mats[s][0] * mats[i][1] * mats[e][1]
        if not memo[s][e] or ret <memo[s][e]:
            memo[s][e] = ret

    return memo[s][e]


N = int(input())
memo = [[0 for _ in range(N)] for _ in range(N)]
mats = []
for _ in range(N):
    mats.append(list(map(int, input().split())))

print(sol(0, N - 1))


#[float 기준 3124ms]================================================
# def sol(s, e):
#     if memo[s][e] == float("inf"):
#         if e - s == 1:
#             memo[s][e] = mats[s][0] * mats[s][1] * mats[e][1]
#         elif s == e:
#             return 0
#         else:
#             for i in range(s, e):
#                 memo[s][e] = min(memo[s][e], sol(s, i) + sol(i + 1, e) + mats[s][0] * mats[i][1] * mats[e][1])
#     return memo[s][e]


# N = int(input())
# memo = [[float("inf") for _ in range(N)] for _ in range(N)]
# mats = []
# for _ in range(N):
#     mats.append(list(map(int, input().split())))
# print(sol(0, N - 1))
#================================
