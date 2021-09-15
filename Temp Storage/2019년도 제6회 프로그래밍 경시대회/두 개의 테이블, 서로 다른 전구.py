# [0. 날짜]
# 2021.09.14(화요일)
# 문제 유형:
# 걸린 시간: 8분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]

# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기] 


def num_to_bin(num):
    s = ""
    while num > 0:
        s += str(num % 2)
        num //= 2
    return s[::-1]

def solution(a, b):
    a_bin, b_bin = num_to_bin(a) , num_to_bin(b)
    if len(a_bin) > len(b_bin):
        while len(b_bin) != len(a_bin):
            b_bin = "0" + b_bin
    elif len(a_bin) < len(b_bin):
        while len(b_bin) != len(a_bin):
            a_bin = "0" + a_bin
    res = 0
    for i in range(len(a_bin)):
        if a_bin[i] != b_bin[i]:
            res += 1
    return res

for _ in range(int(input())):
    print(solution(*map(int, input().split())) )