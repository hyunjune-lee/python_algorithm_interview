# 1. 문자열을 돌리는 거.. 슬라이싱?
# 2. 올바른지 확인하는 거

dic = {"{" : "}", "[" : "]", "(" : ")"}

def solution(s):

    answer = 0
    len_s = len(s)
    for i in range(len_s):
        stack = []
        new_s = s[i:] + s[:i]
        is_right_str = True
        for j in range(len_s):
            if new_s[j] in dic:
                stack.append(new_s[j])
            else:
                if stack:
                    left_bracket = stack.pop()
                else:
                    is_right_str = False
                    break
                if not (left_bracket in dic and dic[left_bracket] == new_s[j]):
                    is_right_str = False
                    break
        if is_right_str and not stack:
            answer += 1

    return answer
