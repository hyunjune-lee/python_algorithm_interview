# 1. 앞에서도 2개씩 잘랐을때 ~ 문자열 길이 반만큼 자르고
# 2. 반복되는만큼 그 자른 단위 만큼 빼주고, 그리고 반복된 자리수 만큼 +1 해주기
#


def solution(s):
    res_str = s
    for word_len in range(1, len(s) // 2 + 1):
        word_count = 1
        prev_word = s[0:word_len]
        zip_str = ""
        for i in range(word_len, len(s), word_len):
            cur_word = s[i : i + word_len]
            if prev_word == cur_word:
                word_count += 1
            else:
                if word_count == 1:
                    zip_str += prev_word
                else:
                    zip_str += str(word_count) + prev_word
                prev_word = cur_word
                word_count = 1
        if word_count == 1:
            zip_str += prev_word
        else:
            zip_str += str(word_count) + prev_word

        if len(res_str) > len(zip_str):
            res_str = zip_str
            # print(zip_str)
    return len(res_str)


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("aaaaaaaaa"))
print(solution("ababababababababab"))
print(solution("ababababababababababab"))
print(solution("a"))
