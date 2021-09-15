# [0. 날짜]
# 2021.09.13(월요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 각 숫자의 인자 중에서 겹치는 것으로만 두 개의 문자열이 나누어지는지 체크
# ---
# 일단 작은거 길이로 나누어지는 체크 => 아니면 작은거 반띵해서 1까지하기 되면 바로 return하기
# replace로 문자열 나누어지는 체크?
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution(L, M):
    min_str = min(L, M)
    max_str = max(L, M)
    res = max_str.replace(min_str, "")
    if len(res) == 0:
        return min_str
    split_len = len(min_str) // 2
    for split_len in range(len(min_str)  // 2 + 1, 0, -1):
        res = max_str.replace(min_str[:split_len], "")
        res2 = min_str.replace(min_str[:split_len], "")
        if len(res) == 0 and len(res2) == 0:
            return min_str[:split_len]
    return ""

for _ in range(int(input())):
    L, M = input().split()
    print(solution(L, M))

# print(solution("KOREATECHKOREATECH", "KOREATECHKOREATECHKOREATECH"))
# print(solution("BYEONGCHEON", "HONGCHEON"))
# print(solution("GURIGURIGURIGURI", "GURIGURI"))
