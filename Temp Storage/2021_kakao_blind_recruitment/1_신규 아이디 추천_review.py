# [0. 날짜]
# 2021.08.19(목요일)
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


def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    new_id = re.sub("[^a-z0-9-_.]", "", new_id)
    # 3
    new_id = re.sub("\.{2,}", ".", new_id)
    # 4
    new_id = re.sub("^\.|\.$", "", new_id)
    # 5
    if not new_id:
        new_id = "a"
    # 6
    new_id = new_id[:15]
    if new_id[-1] == ".":
        new_id = new_id[:-1]
    # 7
    while len(new_id) <= 2:
        new_id += new_id[-1]

    return new_id


print(sol("...!@BaT#*..y.abcdefghijklm"))
print(sol("z-+.^."))
print(sol("=.="))
print(sol("123_.def"))
print(sol("abcdefghijklmn.p"))
