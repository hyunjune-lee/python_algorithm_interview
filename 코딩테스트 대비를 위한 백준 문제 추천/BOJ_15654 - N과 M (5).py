# [0. 날짜]
# 2021.09.27(월요일)
# 문제 유형:
# 걸린 시간: 3분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기] 

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def dfs(l):
    if len(l) == M:
        print(" ".join(l))
    for num in nums:
        num_str = str(num)
        if num_str not in l:
            l.append(num_str)
            dfs(l)
            l.pop()
            
dfs([])

