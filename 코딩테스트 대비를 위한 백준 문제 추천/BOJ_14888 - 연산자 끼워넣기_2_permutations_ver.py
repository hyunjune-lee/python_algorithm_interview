# [0. 날짜]
# 2021.07.14(수요일)
# 문제 유형: 브루트포스 알고리즘, 백트래킹
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# / 할때  cal //= arr[i + 1] 로 해서 틀림 => cal = int(cal / arr[i + 1])


from itertools import permutations


def convert_op_arr_to_str(op_count_arr):
    op_arr = []
    for i, op_count in enumerate(op_count_arr):
        for _ in range(op_count):
            if i == 0:
                op_arr.append("+")
            elif i == 1:
                op_arr.append("-")
            elif i == 2:
                op_arr.append("*")
            elif i == 3:
                op_arr.append("/")
    return op_arr


def solution(N, arr, op_count_arr):
    op_arr = convert_op_arr_to_str(op_count_arr)
    min_val, max_val = +float("inf"), -float("inf")
    op_order = permutations(op_arr, N - 1)
    for op_order in list(set(op_order)):
        cal = arr[0]
        for i, op in enumerate(op_order):
            if op == "+":
                cal += arr[i + 1]
            elif op == "-":
                cal -= arr[i + 1]
            elif op == "*":
                cal *= arr[i + 1]
            elif op == "/":
                cal = int(cal / arr[i + 1])

        min_val = min(min_val, cal)
        max_val = max(max_val, cal)
    print(max_val)
    print(min_val)


solution(N := int(input()), arr := list(map(int, input().split())), op_count_arr := list(map(int, input().split())))
