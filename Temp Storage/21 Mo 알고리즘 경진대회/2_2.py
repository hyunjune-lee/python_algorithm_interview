# [0. 날짜]
# 2021.08.27(금요일)
# 문제 유형: dp
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 바깥쪽의 a를 모두 없앤다.
# 그리고 b를 없애는데 이때 안에 있는 a의 개수와 일치해야 한다.
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# b를 연속으로 붙이는 경우
# 머가 문제지.. => abab 에서 b를 양쪽에 붙이는 경우, 양쪽 끝에서부터의 b의 개수가 다른 케이스 체크 못함

import re


def check(s):
    # 1. 바깥쪽의 a를 모두 없앤다.
    while s != "a":
        # print("1", s)
        s = re.sub("^a*|a*$", "", s)
        # print("2", s)
        if len(s) == 0:
            return True
        # b가 존재하면 b를 없애는데 b의 개수 % 안에 있는 a의 개수 == 0이여야 한다.
        # if s[0] == "b" and s[-1] == "b":
        front_b_idx, back_b_idx = 0, len(s) - 1
        while front_b_idx < len(s) and s[front_b_idx] == "b":
            front_b_idx += 1
        while 0 <= back_b_idx and s[back_b_idx] == "b":
            back_b_idx -= 1
        # 이때 b의 개수도 일치해야되고
        remove_b_count = front_b_idx
        if remove_b_count != len(s) - 1 - back_b_idx or back_b_idx < front_b_idx:
            return False
        a_count = 0
        s = s[front_b_idx : back_b_idx + 1]
        # print("3", s)
        for c in s:
            if c == "a":
                a_count += 1
        if a_count == 0 or remove_b_count < a_count or remove_b_count % a_count != 0:
            return False

    return True


def solution(strs):
    res = []
    for s in strs:
        res.append(check(s))
    return res


"baab"
print(solution(["bbbbbbabababbbbbb", "aaa", "abbabb", "bbabba", "bbbbbbaaabbbbbb", "bbabb"]))
print(solution(["bbb", "baaaba", "bbabbb"]))
# print(solution(["a", "b", "aaa", "bbb", "bbbbabbbb", "abab", "bbaa", "baa", "bababa", "bbbabababbbaa"]))
