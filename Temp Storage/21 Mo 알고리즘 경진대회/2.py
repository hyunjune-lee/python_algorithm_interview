# [0. 날짜]
# 2021.08.27(금요일)
# 문제 유형: dp
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
from collections import deque, defaultdict


s_dict = defaultdict(bool)


def dp():
    q = deque([("a", 1)])
    while q:
        s, x = q.popleft()
        if s_dict[s] or len(s) > 500000:
            continue
        s_dict[s] = True
        # 문자열의 양 옆에 각각 x개만큼의 'b'를 추가합니다.
        q.append(("b" * x + s + "b" * x, x))
        # 문자열의 맨 앞 또는 맨 뒤에 'a'를 추가합니다.
        q.append(("a" + s, x + 1))
        q.append((s + "a", x + 1))


def solution(strs):
    dp()
    for s in strs:
        print(s_dict[s])


print(solution(["abab", "bbaa", "bababa", "bbbabababbbaa"]))
