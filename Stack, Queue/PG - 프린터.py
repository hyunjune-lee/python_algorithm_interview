# [0. 날짜]
# 2021.07.11(일요일) - 10분
# 문제 유형:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution(priorities, location):
    max_order = sorted(priorities, reverse=True)
    print_order = 1
    i = 0
    while print_order <= len(priorities):
        # 지금 출력할 문서이면
        if priorities[i] == max_order[print_order - 1]:
            # 확인할 문서라면
            if i == location:
                return print_order
            # 확인할 문서가 아니라면
            print_order += 1
        i += 1
        if i == len(priorities):
            i = 0


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
