# [0. 날짜]
# 2021.08.27(금요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 일단 set으로 줄이기
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 숫자가 전부 0인것만 들어왔을 떄 마지막에 return num을 안해줘서 틀림

from itertools import combinations, permutations, product
import heapq


def solution(dice):
    dice = [set(d) for d in dice]
    availd_nums = []
    for digit in range(1, len(dice) + 1):
        for com in list(combinations(range(len(dice)), digit)):
            select_dice = []
            for c in com:
                select_dice.append(dice[c])

            for pro in product(*select_dice):
                for per in permutations(pro):
                    if per[0] == 0:
                        continue
                    # print(per, int("".join(map(str, per))))
                    heapq.heappush(availd_nums, int("".join(map(str, per))))
    num = 1
    while availd_nums:
        availd_num = heapq.heappop(availd_nums)
        if num == availd_num:
            num += 1
        elif num < availd_num:
            return num
    return num


print(solution([[0], [0]]))
# print(solution([[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]))
# print(solution([[9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 2, 1]]))
# print(solution([[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5], [6, 3, 4, 7, 6, 5]]))
