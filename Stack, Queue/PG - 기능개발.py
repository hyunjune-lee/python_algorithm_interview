# [0. 날짜]
# 2021.07.11(일요일) - 15분
# 문제 유형: 스택/큐
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 큐를 계속 돌면서 스피드만큼 더해준다.
# 큐의 첫번째가 100 이상이되면 이후 100 미만이 나올때까지 pop해준다.(이때 speed도)
# 그리고 그 개수를 return list에 추가해준다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
# 큐의 첫번째 인자가 며칠뒤에 끝나는지 계산한 후 그만큼 더한 다음에 100미만 나올때까지 pop하면 성능이 향상된다.
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
from collections import deque


def solution(progresses, speeds):
    res_list = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        res = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            res += 1
        if res > 0:
            res_list.append(res)
        for i, speed in enumerate(speeds):
            progresses[i] += speed

    return res_list


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
