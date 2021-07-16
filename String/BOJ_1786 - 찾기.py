# [0. 날짜]
# 2021.07.17(토요일)
# 문제 유형: KMP
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def kmp(text, pattern):
    ans = []
    pi = get_pi(pattern)
    n = len(text)
    m = len(pattern)
    j = 0
    for i in range(0, n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            if j == m - 1:
                ans.append(i - m + 1)
                j = pi[j]
            else:
                j += 1
    return ans


def get_pi(pattern):
    m = len(pattern)
    j = 0
    pi = [0 for _ in range(m)]
    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    return pi


T = input()
P = input()
ans = kmp(T, P)
print(len(ans))
for a in ans:
    print(a + 1, end=" ")
