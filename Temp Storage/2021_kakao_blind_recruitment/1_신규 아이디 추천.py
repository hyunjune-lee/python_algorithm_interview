# 35분
# <오답 노트>
# 1. re.sub(r"\.{2,}", ".", new_id) 에서 re.sub(r"[\.{2,}]", ".", new_id)처럼 []로 묶는 바람에 오류
import re


def solution(new_id):
    # 1 - 소문자로 치환
    new_id = new_id.lower()
    # 2
    new_id = re.sub("[^a-z0-9-_.]", "", new_id)
    # 3
    new_id = re.sub("\.{2,}", ".", new_id)
    # 4
    new_id = re.sub("^\.|\.$", "", new_id)
    # 5
    if len(new_id) == 0:
        new_id = "a"
    # 6
    new_id = new_id[:15]
    new_id = re.sub("\.$", "", new_id)
    # 7
    while len(new_id) <= 2:
        new_id = new_id + new_id[-1]

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
