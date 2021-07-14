# [0. 날짜]
# 2021.07.14(수요일)
# 문제 유형: 구현, 스택, 재귀
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# return res if res != 0 else 1 조건 생각하기가 어려움..
# 음 이걸 제일 안쪽의 괄호일때 더해진게 없어서 0이라 생각하면 좋을듯 그래서 이때 1을 반환해주고
# 아닐때는 지금까지 계산된 값 반환해주기


def dfs(stack, brackets):
    global i
    res = 0
    while i < len(brackets):
        bracket = brackets[i]
        i += 1
        if bracket == "(" or bracket == "[":
            stack.append(bracket)
            delta = dfs(stack, brackets)
            if delta == 0:
                return 0
            elif bracket == "(":
                res += 2 * delta
            elif bracket == "[":
                res += 3 * delta
        else:
            if not stack:
                return 0
            elif bracket == ")" and stack[-1] == "(" or bracket == "]" and stack[-1] == "[":
                stack.pop()
                return res if res != 0 else 1
            else:
                return 0
    if stack:
        return 0
    return res


i = 0
print(dfs([], brackets := input()))
