# [0. 날짜]
# 2021.07.11(일요일)
# 문제 유형:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 다리 큐를 만들어서 길이와 무게가 주어진 것을 넘지 않도록한다.
# 다리에 트럭이 진입할때 pop하는 다음 time을 명시해서 그때가 되면 pop하게 한다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge_queue = deque([])
    truck_weights = deque(truck_weights)
    bridge_weight = 0
    time = 1
    while truck_weights:
        if bridge_queue and bridge_queue[0][1] == time:
            bridge_weight -= bridge_queue.popleft()[0]

        if truck_weights[0] + bridge_weight <= weight and len(bridge_queue) <= bridge_length:
            truck = truck_weights.popleft()
            bridge_queue.append((truck, time + bridge_length))
            bridge_weight += truck
        time += 1

    return bridge_queue[-1][1]


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
