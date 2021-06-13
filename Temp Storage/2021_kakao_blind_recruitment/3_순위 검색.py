from itertools import combinations
import re


def solution(info, query):
    db = {}
    for info_item in info:
        *conditions, score = info_item.split()
        for blank_count in range(5):
            for blank_index_list in combinations(range(4), blank_count):
                cobi = conditions.copy()
                for blank_index in blank_index_list:
                    cobi[blank_index] = "-"
                cobi_key = "and".join(map(str, cobi))
                if cobi_key in db:
                    db[cobi_key].append(int(score))
                else:
                    db[cobi_key] = [int(score)]

    for score_list in db.values():
        score_list.sort()
    answer = []
    for q in query:
        q_score = int(q.split()[-1])
        q = re.sub(" |[0-9]+$", "", q)
        if q in db:
            score_list = db[q]
            start, end = 0, len(score_list)
            while start < end:
                mid = (start + end) // 2
                if score_list[mid] >= q_score:
                    end = mid
                else:
                    start = mid + 1
            answer.append(len(score_list) - end)
        else:
            answer.append(0)
    return answer


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
