# 1. 1이 2개연속으로 한번이라도 나오는 곳부터(안 나오면 그대로 리턴)
# 0의 개수를 세서 개수만큼 세고
# 뒤를 전부 1로바꾼다.
# 앞에서부터 111을 모두 110으로 바꾼다.
import re


def solution(strs):
    res_list = []
    for s in strs:
        # print(s)
        m = re.search("11", s)
        if m:
            start = m.start()
            one_count = s[start:].count("1")
            zero_count = s[start:].count("0")
            if one_count // 2 < zero_count:
                zero_count = one_count // 2
            change_str = "1" * (len(s) - m.start())
            res = s[:start] + change_str.replace("111", "110", zero_count)
            res_list.append(res)
        else:
            res_list.append(s)
    return res_list


print(solution(["1110", "100111100", "0111111010", "00000", "1010", ""]))
