# 1. 연산자 set 확인, 우선순위 정하기
# 2. stack 중위 연산 구현하기
# 35~40분
# 괜히 stack 중위 연산을 생각해서 시간이 좀 걸렸고
# 중간에 exp값이 잘 나오는지 체크를 잘못함 마지막 operand가 안 붙는 걸 못봄


def solution(expression):
    def dfs(expr_rank):
        if len(expr_rank) == len(expr_set):
            expr_rank_list.append(expr_rank)
            return
        for e in expr_list:
            if e not in expr_rank:
                dfs(expr_rank + [e])

    def oper(o1, o2, op):
        if op == "-":
            return o1 - o2
        elif op == "+":
            return o1 + o2
        elif op == "*":
            return o1 * o2
        else:
            print("error")

    expr = ["*", "-", "+"]
    expr_set = set()
    expr_rank_list = []
    for c in expression:
        if c in expr:
            expr_set.add(c)
    expr_list = list(expr_set)
    dfs([])
    exp = []
    word = ""
    for c in expression:
        if c in expr:
            if len(word) > 0:
                exp.append(int(word))
            exp.append(c)
            word = ""
        else:
            word += c
    if len(word) > 0:
        exp.append(int(word))
    print(exp)

    max_res = 0
    for expr_rank in expr_rank_list:
        new_exp = exp[:]
        for op in expr_rank:
            i = 0
            while i < len(new_exp):
                e = new_exp[i]
                if e == op:
                    res = oper(new_exp[i - 1], new_exp[i + 1], op)
                    for _ in range(3):
                        new_exp.pop(i - 1)
                    new_exp.insert(i - 1, res)
                    i -= 1
                    print(new_exp)
                i += 1
        max_res = max(max_res, abs(new_exp[0]))

    return max_res


solution("100-200*300-500+20")
