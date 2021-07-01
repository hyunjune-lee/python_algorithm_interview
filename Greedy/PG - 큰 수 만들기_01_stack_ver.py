# [0. 날짜]
# 2021.07.01(목요일)
# 문제 유형: Greedy
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution(number, k):
    stack = [number[0]]
    count_k = k
    for num in number[1:]:
        while stack and stack[-1] < num and count_k > 0:
            stack.pop()
            count_k -= 1
        stack.append(num)
    return "".join(stack[0 : len(number) - k])


print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
