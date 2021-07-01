# [0. 날짜]
# 2021.07.01(목요일)
# 문제 유형: Greedy
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 1. A를 원하는 단어로 바꾸는 측면이 아닌 원하는 단어를 A로 바꾸는 방법으로 접근해본다.
# 1. 우리는 A가 아닌 개수만큼만 바꾼다.
# 2. 바꿀때 드는 조이스틱을 위 아래로 움직이는 비용과 좌우 이동 비용을 계산한다.
# 2-1. 좌우 이동은 near_not_a_i로 계산한다. 좌우로 했을 때 가장 가까운 i를 찾는다.
# 2-2. 상하 이동은 A로부터 변환할때, Z로부터로 변환할때 + 1를 비교해서 구한다.
# 3. 해당 인덱스는 A로 바꾼다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# cycle_name 설정할때.. name + name으로 했다. 이러면 위로 index가 넘어갈때 runtime에러가 나온다.
# name + name + name으로 해줘야 한다..

from collections import Counter


def near_not_a_i(name, cur_i):
    i = len(name) + cur_i
    cycle_name = name + name + name
    for delta in range(0, len(name)):
        if cycle_name[i + delta] != "A":
            next_i = i + delta - len(name)
            return (next_i if next_i < len(name) else next_i - len(name), delta)
        elif cycle_name[i - delta] != "A":
            next_i = i - delta - len(name)
            return (next_i if next_i >= 0 else next_i + len(name), delta)


def solution(name):
    name = [c for c in name]
    res = 0
    i = 0
    change_limit = len(name) - Counter(name)["A"]
    # 가장 가까운 A가 아닌 지점으로 가는 법
    change_cnt = 0
    while change_cnt < change_limit:
        i, move_cost = near_not_a_i(name, i)
        # 상향식 값
        up_cost = abs(ord("A") - ord(name[i]))
        # 하향식 값
        down_cost = abs(ord("Z") - ord(name[i])) + 1
        res += min(up_cost, down_cost) + move_cost
        name[i] = "A"
        change_cnt += 1

    return res


print(solution("ZZZZZZZZZZZZZZZZ"))
# print(solution("AAAAAAAAAAAAAZZAAAAAAA"))
# print(solution("AAAAAAAAAAAAAZZAAA"))
# print(solution("JAZ"))
# print(solution("AAZ"))
# print(solution("JEROEN"))
# print(solution("JAN"))
