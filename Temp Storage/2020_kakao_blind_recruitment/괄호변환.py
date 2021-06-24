def is_right(s):
    stack = []
    i = 0
    while i < len(s):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if stack:
                if stack.pop() != "(":
                    return False
            else:
                return False
        i += 1

    if stack:
        return False
    return True


def split_uv(str):
    i = 0
    right_bracket = 0
    left_bracket = 0
    while i == 0 or left_bracket != right_bracket:
        if str[i] == "(":
            left_bracket += 1
        else:
            right_bracket += 1
        i += 1
    return str[:i], str[i:]


def make_balance(p):
    if not p:
        return p
    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u, v = split_uv(p)
    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
    # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
    if is_right(u):
        return u + make_balance(v)
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        # 4-3. ')'를 다시 붙입니다.
        temp_str = "(" + make_balance(v) + ")"
        new_u = ""
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고,
        # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        for c in u[1 : len(u) - 1]:
            if c == "(":
                new_u += ")"
            else:
                new_u += "("
        return temp_str + new_u


def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if not p:
        return p
    return make_balance(p)


print(solution(""))
print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))
