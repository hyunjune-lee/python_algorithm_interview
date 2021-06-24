# 언어 : Python
# 날짜 : 2021.06.24
# 문제 : Programmers > Lv2 > 메뉴 리뉴얼
# 출처 : 2021 KAKAO BLIND RECRUITMENT
# ================================================
# 개선 방법 : Counter 사용하기
# ================================================
from itertools import combinations
from collections import Counter


def solution(orders, course):
    result = []

    # 각 course 값에 대해 코스요리 후보 구하기
    for size in course:
        # 크기가 현재 course의 size인 모든 조합 구하기
        order_combinations = []
        for order in orders:
            # for x in combinations(sorted(order), size):
            #     print(x)
            # order_combinations.extend(list(combinations(sorted(order), size)))
            order_combinations.append(list(combinations(sorted(order), size)))
            # print("append:", order_combinations, "\n")
            # order_combinations += combinations(sorted(order), size)
            # print("+=", order_combinations)

        # 해당 course에서 가장 많이 주문된 메뉴 조합을 찾아서 result에 저장
        most_ordered = Counter(order_combinations).most_common()
        for menu, ordered_num in most_ordered:
            if ordered_num > 1 and ordered_num == most_ordered[0][1]:
                result.append("".join(menu))
    return sorted(result)


# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
# orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
answer = solution(orders, course)
print(answer)
