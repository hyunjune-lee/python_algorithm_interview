# [0. 날짜]
# 2021.07.22(목요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]\
# 1. 1을 더하는
# 2번과 3번 동작은 같이 묶어서 봐야햔다.
# 2 + 3. 동작을 2더한곳에 현재의 A개수를 버퍼에 넣어줌
# (dp 구성요소)
# 행동개수(인덱스) + 화면의 글자 개수하고 버퍼의 개수를 메모이제이션
# 그래서 결론
# 1. 글자를 1개 더할지
# 2. 복사를 할지
# 3. 버퍼만큼 출력할지 계산
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 복사할때 다음 buf 개수가 a_cnt가 되어야하는데... buf + a_cnt로 해줬다..
from collections import deque


def solution():
    # 복사할때 2칸 뒤에 적어서 좀 더 여유있게 dp 생성
    dp = [[0, 0] for _ in range(N + 2)]
    q = deque([(0, 0, 0)])
    max_a_cnt = 0
    while q:
        idx, a_cnt, buf = q.popleft()
        if idx == N:
            max_a_cnt = max(max_a_cnt, a_cnt)
            continue
        if (a_cnt, buf) in dp[idx]:
            continue
        dp[idx].append((a_cnt, buf))
        if idx + 1 <= N:
            q.append((idx + 1, a_cnt + max(1, buf), buf))
        if idx + 2 <= N:
            q.append((idx + 2, a_cnt, a_cnt))

    return max_a_cnt


N = int(input())
print(solution())


# def solution():
#     # 복사할때 2칸 뒤에 적어서 좀 더 여유있게 dp 생성
#     dp = [[0, 0] for _ in range(N + 2)]
#     for x in range(N):
#         # 1. 글자를 1개 더하거나 버퍼에 있는 만큼 넣는다. 이때 최대가 되도록
#         dp[x + 1][0] = dp[x][0] + max(1, dp[x][1])
#         # 복사를한다.
#         dp[x + 2][1] = dp[x][0]
#         print(dp)
#     return dp[N][0]
