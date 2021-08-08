# 참고 - https://huiung.tistory.com/121
# [0. 날짜]
# 2021.07.24(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# cache로 해당 열에 이름을 썼을 때의 빈공간
# (분기점)
# 1. 계속 쓸지
# 2. 다음 줄에 쓸지
# (sol 인자)
# 열 위치, 이름의 인덱스
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def sol(col, name_idx):
    # 이름을 다 썼다면 마지막 줄은 count 하지 않는다.
    if name_idx == n:
        return 0
    res = dp[col][name_idx]
    if res != -1:
        return res
    # 다음행에 지금 이름 쓰기(길이하고 인덱스하고 차이 때문에 결국 + 1)
    res = sol(names[name_idx] + 1, name_idx + 1) + (m - col + 1) ** 2

    # 쓸 수 있다면 지금행에 이름 쓰기
    if col + names[name_idx] - 1 <= m - 1:
        res = min(res, sol(col + names[name_idx] + 1, name_idx + 1))
    dp[col][name_idx] = res
    return res


# n 이름의 길이들, m은 가로 칸의 개수
n, m = map(int, input().split())
names = []
for _ in range(n):
    names.append(int(input()))

dp = [[-1 for _ in range(n)] for _ in range(m + 2)]

print(sol(names[0] + 1, 1))
