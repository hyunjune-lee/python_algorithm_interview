# [0. 날짜]
# 2021.09.09(목요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

import re


def solution(user_id, banned_id):
    ban_match_list = []
    for b_id in banned_id:
        b_id = re.sub("\\*", ".", "".join(b_id))
        r = []
        for u_id in user_id:
            if re.match(b_id, u_id) and len(b_id) == len(u_id):
                r.append(u_id)
        ban_match_list.append(r)

    res = set()

    def dfs(i, visited):
        if i == len(banned_id):
            res.add(tuple(sorted(visited)))
            return
        for b_id in ban_match_list[i]:
            if b_id not in visited:
                visited.append(b_id)
                dfs(i + 1, visited)
                visited.pop()
        return

    dfs(0, [])

    return len(res)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
