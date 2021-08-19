# [0. 날짜]
# 2021.08.06(금요일)
# 문제 유형: DP
# 걸린 시간: 1시간
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# Scv의 체력이 60이므로
# Scv의 개수만큼의 차원 배열을 만듭니다 개수가 2개면 2차원 3개면 3차원으로
# 그리고 bfs로 완전탐색에 메모이제이션을 적용해서 풉니다
# bfs 돌때 첫번째 scv, 두번째 scv, 세번쨰 scv로 공격하는 경우의 수를 탐색합니다.
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 메모이제이션을 일관되게 조회하기 위해서 scvs_health 리스트의 길이를 3개로 맞춰주었다.
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from collections import deque


def sol():
    damage_cases = []

    def dfs(visited):
        if len(visited) == N:
            damage_cases.append(visited[:])
        for i in range(N):
            damage = [9, 3, 1][i]
            if damage not in visited:
                visited.append(damage)
                dfs(visited)
                visited.pop()

    dfs([])
    damage_memo = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]
    q = deque([(scvs_health, 0)])
    while q:
        cur_scvs_health, attack_cnt = q.popleft()
        a, b, c = cur_scvs_health
        if not any(cur_scvs_health):
            return attack_cnt
        for damage_case in damage_cases:
            next_scvs_health = []
            for i in range(N):
                health = cur_scvs_health[i] - damage_case[i]
                next_scvs_health.append(health if health > 0 else 0)
            for _ in range(3 - N):
                next_scvs_health.append(0)
            na, nb, nc = next_scvs_health
            if damage_memo[na][nb][nc]:
                continue
            damage_memo[na][nb][nc] = 1
            q.append((next_scvs_health, attack_cnt + 1))


N = int(input())  # SCV의 수
scvs_health = list(map(int, input().split()))
for _ in range(3 - N):
    scvs_health.append(0)
print(sol())
