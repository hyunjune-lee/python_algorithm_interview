from collections import defaultdict
import re


def solution(str1, str2):
    dic_all = defaultdict(int)
    dic1 = defaultdict(int)
    for i in range(len(str1) - 1):
        word = str1[i : i + 2].lower()
        if word[0].isalpha() and word[1].isalpha():
            dic1[word] += 1
            dic_all[word] += 1
    print(dic1)
    dic2 = defaultdict(int)
    for i in range(len(str2) - 1):
        word = str2[i : i + 2].lower()
        if word[0].isalpha() and word[1].isalpha():
            dic2[word] += 1
            dic_all[word] += 1

    if len(dic_all) == 0:
        return 65536

    a = 0
    b = 0
    for word in dic_all:
        a += min(dic1[word], dic2[word])
        b += max(dic1[word], dic2[word])
    # print(a, b)
    return int((a / b) * 65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
