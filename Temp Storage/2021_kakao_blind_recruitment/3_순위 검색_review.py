# [0. 날짜]
# 2021.08.27(금요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from itertools import combinations
from collections import defaultdict
import re


def binary_search(score_list, score):
    l, r = 0, len(score_list)
    while l < r:
        mid = (l + r) // 2
        if score_list[mid] >= score:
            r = mid
        else:
            l = mid + 1
    return l


def solution(infos, queries):
    query_dict = defaultdict(list)
    for info in infos:
        *info_item, score = info.split()
        for dash_count in range(5):
            for dash_pos_list in combinations(range(4), dash_count):
                new_info_item = info_item[:]
                for dash_pos in dash_pos_list:
                    new_info_item[dash_pos] = "-"
                query_dict[" and ".join(new_info_item)].append(int(score))
    for score_list in query_dict.values():
        score_list.sort()

    res = []
    for query in queries:
        key = re.sub(" [0-9]+$", "", query)
        score = int(query.split()[-1])
        lower_bound = binary_search(query_dict[key], score)
        res.append(len(query_dict[key]) - lower_bound)
    return res


print(
    solution(
        [
            "java backend junior pizza 150",
            "python frontend senior chicken 210",
            "python frontend senior chicken 150",
            "cpp backend senior pizza 260",
            "java backend junior chicken 80",
            "python backend senior chicken 50",
        ],
        [
            "java and backend and junior and pizza 100",
            "python and frontend and senior and chicken 200",
            "cpp and - and senior and pizza 250",
            "- and backend and senior and - 150",
            "- and - and - and chicken 100",
            "- and - and - and - 150",
        ],
    )
)
