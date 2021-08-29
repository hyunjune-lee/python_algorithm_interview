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


memo_dict = defaultdict(bool)


def dfs(x, y):
    # print(x)
    # key = " ".join(map(str, x))
    # print("key", key)
    # if memo_dict[key]:
    #     return False
    # memo_dict[key] = True

    if len(x) == len(y):
        if sorted(x) == y:
            return True
        return False

    max_y = max(y)
    visited = []
    for comb in combinations(range(len(x)), 2):
        visit = set([x[comb[0]], x[comb[1]]])
        if visit in visited:
            continue
        visited.append(visit)
        sum_x = x[comb[0]] + x[comb[1]]
        if sum_x > max_y:
            continue
        new_x = [sum_x]
        for i in range(len(x)):
            if i not in comb:
                new_x.append(x[i])
        if dfs(new_x, y):
            return True

    return False


def solution(p, q):

    res = []
    for i in range(len(p)):

        res.append(dfs(p[i], sorted(q[i])))

    return res


# print([2, 7] == [2, 7])
print(solution([[5, 3, 2, 2, 1]], [[7, 2, 4]]))
print(solution([[4, 3, 3], [1, 2, 3], [3, 2, 4]], [[5, 5], [5, 1], [1, 8]]))
