# [0. 날짜]
# 2021.07.13(화요일)
# 문제 유형: 수학, 구현
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def find_max_people_count():
    people_count = 0
    max_people_count = -1
    for _ in range(10):
        leave, ride = map(int, input().split())
        people_count -= leave
        people_count += ride
        max_people_count = max(max_people_count, people_count)
    return max_people_count


print(find_max_people_count())
