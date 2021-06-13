# 25분
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    cours_dict = defaultdict(int)
    for course_count in course:
        for order in orders:
            for new_course in combinations(order, course_count):
                new_course_name = "".join(map(str, sorted(new_course)))
                cours_dict[new_course_name] += 1
        values = cours_dict.values()
        if values:
            max_order = max(cours_dict.values())
            max_order = max_order if max_order >= 2 else -1
            for new_cours in cours_dict.items():
                if new_cours[1] == max_order:
                    answer.append(new_cours[0])
        cours_dict = defaultdict(int)
    for new_cours in cours_dict.items():
        if new_cours[1] > 2:
            print(new_cours[0])
    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
