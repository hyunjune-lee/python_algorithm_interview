# [0. 날짜]
# 2021.08.21(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 뭔가 부분집합에 따라 dp를 알면 좋을거 같은데
# ab는
# a O + b O
# a O + b X
# a X + b O
# a X + b X
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


from collections import defaultdict

memo = defaultdict(list)


def dp(s):
    if memo[s]:
        print(s)
        return memo[s]
    if len(s) == 1:
        memo[s] = ["", s]
        return ["", s]
    else:
        res = set()
        # a O + b O
        a_subset = dp(s[:1])
        b_subset = dp(s[1:])
        for a in a_subset:
            for b in b_subset:
                ab = list(a) + list(b)
                ab.sort()
                res.add("".join(ab))
            # a O + b X
            res.add(a)
        # a X + b O
        for b in b_subset:
            res.add(b)
    memo[s] = res
    return res


def solution(orders, course):
    order_count_dict = defaultdict(int)
    course_count = [[] for _ in range(11)]
    for order in orders:
        for order_subset in dp(order):
            if len(order_subset) >= 2:
                order_count_dict[order_subset] += 1
    for course_candidate, order_count in order_count_dict.items():
        if order_count >= 2 and len(course_candidate) in course:
            course_count[len(course_candidate)].append((course_candidate, order_count))

    for c_cnt in course_count:
        c_cnt.sort(key=lambda x: x[1])

    res = []
    for c in course:
        if course_count[c]:
            max_cnt = course_count[c][-1][1]
            while course_count[c] and course_count[c][-1][1] == max_cnt:
                res.append(course_count[c].pop()[0])

    return sorted(res)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
