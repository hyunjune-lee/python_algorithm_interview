# 1. 연산자 set 확인, 우선순위 정하기
# 2. stack 중위 연산 구현하기
# 35~40분
# 괜히 stack 중위 연산을 생각해서 시간이 좀 걸렸고
# 중간에 exp값이 잘 나오는지 체크를 잘못함 마지막 operand가 안 붙는 걸 못봄
# 순열하고, eval 사용법을 몰라서ㅠㅠ
from itertools import permutations
import re


def solution(expression):
    op = [x for x in ["*", "-", "+"] if x in expression]
    op_rank = list(permutations(op))

    # expr = re.split(r"(\D)", expression)
    expr = re.split(r"([^0-9])", expression)
    print(expr)
    max_res = 0
    for op_list in op_rank:
        new_expr = expr[:]
        for op in op_list:
            while op in new_expr:
                i = new_expr.index(op)
                new_expr[i - 1] = str(eval(new_expr[i - 1] + op + new_expr[i + 1]))
                new_expr = new_expr[:i] + new_expr[i + 2 :]
        max_res = max(max_res, abs(int(new_expr[0])))

    return max_res


print(solution("100-200*300-500+20"))
