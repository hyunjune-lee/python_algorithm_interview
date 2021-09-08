# [0. 날짜]
# 2021.09.06(월요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 
# [3. +개선 사항]
# 가장 많은 순서대로 리스트에 담아도 되는구나
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 집합의 개수가 s라고 생각해서 1,000,000개일때 시간초과가 안 날거 같은 알고리즘을 찾았는데
# 자세히 보니 문자열의 개수 1,000,000개였다...


def solution(s):
    sets = eval(s[1:-1])
    if len(sets) == 1:
        return list(sets)
    set_list = sorted(list(sum(set) for set in sets))
    res = [set_list[0]]
    for i in range(1, len(set_list)):
        res.append(set_list[i] - set_list[i - 1])
    return res


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
