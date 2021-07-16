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
    pi = get_pi(pattern)
    pattern_len = len(pattern)
    j = 0
    for i in range(text_len := len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            if j == pattern_len - 1:
                return 1
            else:
                j += 1
    return 0


def get_pi(pattern):
    pattern_len = len(pattern)
    j = 0
    pi = [0 for _ in range(pattern_len)]
    for i in range(1, pattern_len):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi


print(kmp(S := input(), P := input()))
