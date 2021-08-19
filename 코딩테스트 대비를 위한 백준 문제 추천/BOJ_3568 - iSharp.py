# [0. 날짜]
# 2021.08.01(일요일)
# 문제 유형: 26분
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# int& a*[]&, b, c*; 를 공백으로 잘랐을 때
# 첫번째 span은 각각 정답의 앞에 붙이고
# 그뒤의 각각 span에 대해 뒤에서부터 붙여준다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
# 정규식을 사용하면 더 깔끔한 풀이가 될거 같다.
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 변수명이 한글자라고 생각했다.. 문제를 꼼꼼하게 읽자


def sol(line):
    default_var_type = line[0]
    for i in range(1, len(line)):
        span = line[i][:-1]
        res = default_var_type[:]
        var_name = ""
        for span_i in range(len(span) - 1, -1, -1):
            c = span[span_i]
            if c == "]":
                res += "[]"
            elif c == "[":
                pass
            elif c == "*" or c == "&":
                res += c
            else:
                var_name = span[0 : span_i + 1]
                break
        print(res + " " + var_name + ";")


sol(input().split(" "))
