# [0. 날짜]
# 2021.07.24(토요일)
# 문제 유형: DP
# 걸린 시간: 1시간 10분..
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 1. 먼저 객차의 각 인덱스마다 객차가 되었을 때의 운송량을 슬라이딩 윈도우로 구한다.
# 2. dp를 0 - 1 배낭을 응용해서 y를 객차가 1개일 때, 객차가 2개일 때, 객차가 3개일 때 , x는 객차 index
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 2개일 때 1개일 때의 최대 dp 탐색하고 + 0개일 때의 차량을 탐색하는 것
# 3개일 떄도 2개일 때 car_allow 이전의 최대 dp 탐색 + 0개일 때의 차량을 탐색하는 것
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def sol():
    # 1. 먼저 객차의 각 인덱스마다 객차가 되었을 때의 운송량을 슬라이딩 윈도우로 구한다.
    dp = [[0 for _ in range(N)] for _ in range(4)]
    dp[0][0] = sum(car_vols[:car_allow])  # 객차가 1개일때 각 인덱스별 운송량
    for left in range(N - car_allow):
        right = left + car_allow
        dp[0][left + 1] = dp[0][left] - car_vols[left] + car_vols[right]
    # print(dp[0])
    # 2. dp를 0 - 1 배낭을 응용해서 y를 객차가 1개일 때, 객차가 2개일 때, 객차가 3개일 때 , x는 객차 index
    for y in range(1, 4):
        for x in range((y - 1) * car_allow, N):
            if x - car_allow < 0:
                dp[y][x] = dp[y - 1][x]
            else:
                if y == 1:
                    dp[y][x] = max(dp[y][x - 1], dp[0][x])
                else:
                    dp[y][x] = max(dp[y][x - 1], dp[y - 1][x - car_allow] + dp[0][x])
        # print(dp[y])
    return dp[3][N - car_allow]


N = int(input())
car_vols = list(map(int, input().split()))
car_allow = int(input())

print(sol())
