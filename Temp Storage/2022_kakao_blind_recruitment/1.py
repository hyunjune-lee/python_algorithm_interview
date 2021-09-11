# [0. 날짜]
# 2021.09.11(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from collections import defaultdict


def solution(id_list, report, k):
    report_dict = defaultdict(set)
    report_cnt_dict = defaultdict(int)
    report_res_count = dict()
    for id in id_list:
        report_res_count[id] = 0

    for r in report:
        user_id, report_id = r.split()
        if report_id not in report_dict[user_id]:
            report_dict[user_id].add(report_id)
            report_cnt_dict[report_id] += 1

    res_list = []
    for id in id_list:
        res = 0
        for report_id in report_dict[id]:
            if report_cnt_dict[report_id] >= k:
                res += 1

        res_list.append(res)
    return res_list


print(
    solution(
        ["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2
    )
)
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
