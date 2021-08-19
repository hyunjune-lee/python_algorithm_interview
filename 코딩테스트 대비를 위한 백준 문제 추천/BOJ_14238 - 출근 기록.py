# [0. 날짜]
# 2021.08.10(화요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# memo = [전전날][전날][오늘 남은 A 출근날][오늘 남은 B 출근날][오늘 남은 C 출근날]
# 있으면 return 0
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# memo 위치를 for문 들어가기전에 해줘야 하는데..
# for문안에서 해버렸다..
from collections import defaultdict


def abc_to_int(char):
    if char == "A":
        return 1
    elif char == "B":
        return 2
    elif char == "C":
        return 3
    elif char == " ":
        return 0


def sol(n):
    if n - 2 == len(input_remain):
        return 1
    memo_res = memo[abc_to_int(work_record[n - 2])][abc_to_int(work_record[n - 1])][abc[1]][abc[2]][abc[3]]
    if memo_res:
        return 0
    memo[abc_to_int(work_record[n - 2])][abc_to_int(work_record[n - 1])][abc[1]][abc[2]][abc[3]] = 1
    for i, staff in enumerate("ABC"):
        if abc[i + 1] > 0 and dp[n][i]:
            for j in range(i):
                dp[n + j + 1][i] = False
            work_record.append(staff)
            abc[i + 1] -= 1
            if sol(n + 1):
                return 1
            for j in range(i):
                dp[n + j + 1][i] = True
            abc[i + 1] += 1
            work_record.pop()

    return 0


dp = [[True, True, True] for _ in range(55)]
memo = [[[[[0 for _ in range(55)] for _ in range(55)] for _ in range(55)] for _ in range(4)] for _ in range(4)]
input_remain = list(input())
abc = [0, 0, 0, 0]
for c in input_remain:
    num = abc_to_int(c)
    abc[num] += 1

work_record = [" ", " "]
if sol(2):
    print("".join(work_record[2:]))
else:
    print(-1)
