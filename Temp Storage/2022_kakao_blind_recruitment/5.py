# [0. 날짜]
# 2021.09.11(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 0단계 이미 접근 상태
# 현재 개방된 노드로부터 1 단계(바로 접근 가능), 2단계(한노드 건너야 가능)
# 2단계이면 현재 양의 개수가 늑대보다 2개 더 많아야한다.
# 3단계이면 3개 더 많아야한다.
# 그리디스럽게?
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

from collections import defaultdict, deque


def solution(info, edges):
    wolf_dict = defaultdict(int)
    binary_tree = defaultdict(list)
    for i, info_item in enumerate(info):
        wolf_dict[i] = info_item

    for parent, child in edges:
        binary_tree[parent].append(child)
    print(binary_tree)
    q = deque([0])
    visited = [0]
    wolf_cnt = 0
    sheep_cnt = 0
    access_list = []
    while q:
        node = q.popleft()
        if wolf_dict[node]:
            wolf_cnt += 1
        else:
            sheep_cnt += 1
        print(sheep_cnt, wolf_cnt)
        for child in binary_tree[node]:
            if wolf_dict[child]:  # 늑대면
                access_list.append(child)
            else:  # 양이면..
                q.append(child)
                visited.append(child)
    visited = [0]

    answer = 0
    return answer


print(
    solution(
        [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]],
    )
)
print(
    solution(
        [0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]],
    )
)
