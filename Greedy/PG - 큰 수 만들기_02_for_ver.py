# [0. 날짜]
# 2021.07.01(목요일)
# 문제 유형: Greedy
# stack_ver 보다 훨씬 느린 풀이이다..
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 일단 숫자의 자릿수가 큰게 무엇보다 우선이므로
# 뒤에서부터 최대자릿수를 유지하는 최소 숫자들을 남겨두고 그중에서 최대 숫자를 찾아서 결과값에 찾아준다.
# 그리고 그 뒤부터 최대 숫자를 찾느다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 슬라이싱 해서, max_num == 9일떄 바로 종료 조건 안 넣어서 시간 초과


def solution(number, k):
    number_list = [int(num) for num in number]
    res_digit = len(number) - k
    res_num = ""
    start_i = 0
    for end_gap in range(res_digit - 1, -1, -1):  # 4,3,2,1
        max_num = -1
        next_start_i = start_i
        for i in range(start_i, len(number) - end_gap):
            if max_num < number_list[i]:
                max_num = number_list[i]
                next_start_i = i + 1
                if max_num == 9:
                    break
        res_num += str(max_num)
        start_i = next_start_i
    return res_num


# print(solution("1924", 2))
# print(solution("1231234", 3))
print(solution("4177252841", 4))
