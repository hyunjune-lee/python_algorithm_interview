# [0. 날짜]
# 2021.09.15(수요일)
# 문제 유형:
# 걸린 시간: 40분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기] 
# 마지막 문자열까지 해서 총 9개의 문자열이 전부 주어지는데
#     str_set |= set(q_str) 를 안해줬다.

from itertools import permutations

for _ in range(int(input())):
    inputs = input().split()
    str_cnt = int(inputs[0])
    inputs = inputs[1:]
    q_str = inputs[-1]
    str_dict = dict()
    str_set = set()
    for i in range(str_cnt):
        strs = inputs[2* i]
        num = int(inputs[2 * i + 1])
        str_dict[strs] = num
        str_set |= set(strs)
    str_set |= set(q_str)
    # print(str_dict)
    str_list = list(str_set)
    # for i in range(9 - len(str_list)):
    #     str_list.append(str(i))
    possible_dict = dict()
    for per in permutations(range(1,10), 9):
        is_ok = True
        for i in range(9):
            possible_dict[str_list[i]] = per[i]
        for str_elems, num in str_dict.items():
            check_num =0
            for str_elem in str_elems:
                check_num += possible_dict[str_elem]
            if num != check_num:
                is_ok = False
                break
        if is_ok:
            res = 0
            for c in q_str:
                res += possible_dict[c]
            print(res)
            break
        


