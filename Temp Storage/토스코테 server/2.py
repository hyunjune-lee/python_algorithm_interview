from collections import deque
from collections import defaultdict


def solution(servers, sticky, requests):
    answer = [[] for _ in range(servers)]
    load_index = servers - 1
    requests = deque(requests)
    before_request_server = dict()
    while requests:
        request = requests.popleft()
        if sticky and request in before_request_server:
            answer[before_request_server[request]].append(request)
            continue
        load_index += 1
        if load_index == servers:
            load_index = 0
        answer[load_index].append(request)
        before_request_server[request] = load_index

    return answer


print(solution(2, False, [1, 2, 3, 4]))
print(solution(2, True, [1, 1, 2, 2]))
print(solution(2, True, [1, 2, 2, 3, 4, 1]))
print(solution(4, True, [1, 2, 2, 3, 4, 1]))
