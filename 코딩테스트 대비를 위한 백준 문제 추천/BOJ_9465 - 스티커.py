# [0. 날짜]
# 2021.09.27(월요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# dp
# [3. +개선 사항]
# dp에 0을 넣어서 index를 밀어서 시작하는 테크닉
# [4. +한번에 맞추지 못한 경우 오답 원인 적기] 
# print(max(a[0] + b[1], b[0] + a[1]))로 해야되는데 중간에 + 대신에 , 로 넣거나
# continue로 빼먹었다.


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n == 1:
        print(max(a[0], b[0]))
        continue
    elif n == 2:
        print(max(a[0] + b[1], b[0] + a[1]))
        continue
    a[1] += b[0]
    b[1] += a[0]
    for x in range(2, n):
        a[x] += max(b[x-1], a[x-2], b[x-2])
        b[x] += max(a[x-1], b[x-2], a[x-2])
    print(max(a[n- 1], b[n - 1]))