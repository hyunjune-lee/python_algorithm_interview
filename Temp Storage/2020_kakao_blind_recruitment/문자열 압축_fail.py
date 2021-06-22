# 1. 앞에서도 2개씩 잘랐을때 ~ 문자열 길이 반만큼 자르고
# 2. 반복되는만큼 그 자른 단위 만큼 빼주고, 그리고 한번만 +1 해주기


def solution(s):
    res = len(s)
    for word_len in range(1, len(s) // 2 + 1):
        i = word_len
        zip_len = len(s)
        while i < len(s):
            is_same_word = True
            for _ in range(word_len):
                if i >= len(s) or s[i] != s[i - word_len]:
                    is_same_word = False
                i += 1
            if is_same_word:  # 같은 문자열이 반복되면 숫자가 들어가면서 +1
                zip_len += 1
                zip_len -= word_len
            if i >= len(s):
                break
            while is_same_word:
                for _ in range(word_len):
                    if i >= len(s) or s[i] != s[i - word_len]:
                        is_same_word = False
                    i += 1
                if is_same_word:
                    zip_len -= word_len
                if i >= len(s):
                    break
        res = min(zip_len, res)
    return res


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("aaaaaaa"))
