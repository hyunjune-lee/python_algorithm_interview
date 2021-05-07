# 한번 구간을 찾은 이후로는 그 구간 길이 이상은 탐색ㄴㄴ
# 처음 1개씩 다 있을 될 때까지 가면서 개수를 세고
#

from collections import Counter


def solution(gems):
    need = dict()
    for gem in set(gems):
        need[gem] = 1
    missing = len(need)
    left = start = end = 0
    for right, char in enumerate(gems, 1):
        missing -= need[char] > 0
        need[char] -= 1

        if missing == 0:
            while left < right and need[gems[left]] < 0:
                need[gems[left]] += 1
                left += 1

            if not end or right - left < end - start:
                end, start = right, left
                need[gems[left]] += 1
                missing += 1
                left += 1

    return start + 1, end


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
