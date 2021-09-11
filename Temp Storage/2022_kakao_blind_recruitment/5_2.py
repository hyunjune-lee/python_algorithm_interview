# [0. 날짜]
# 2021.09.11(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 완전탐색??
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


from collections import defaultdict, deque

max_sheep_cnt = 0


def solution(info, edges):
    wolf_dict = defaultdict(int)
    binary_tree = defaultdict(list)
    max_sheep_dict = defaultdict(list)
    for i, info_item in enumerate(info):
        wolf_dict[i] = info_item

    for parent, child in edges:
        binary_tree[parent].append(child)

    # print(binary_tree)
    # print(reverse_tree)
    # dfs로 각 노드에서 최대 얻을 수 있는 sheep 개수(가능성)를 체크해본다. 가지치기와 우선순위를 위해서?
    def max_sheep_check(node):
        ret = 0
        if not wolf_dict[node]:
            ret += 1
        if len(binary_tree[node]) == 0:
            max_sheep_dict[node] = ret
            return ret

        for child in binary_tree[node]:
            ret += max_sheep_check(child)
        max_sheep_dict[node] = ret
        return ret

    max_sheep_check(0)
    # print("max_sheep_dict", max_sheep_dict)
    global max_sheep_cnt
    max_sheep_cnt = 0

    history = []

    def dfs(node, sheep_cnt, wolf_cnt, access_list, visited):
        global max_sheep_cnt

        # visited.append(node)

        if wolf_dict[node]:
            wolf_cnt += 1
        else:
            sheep_cnt += 1
        if sheep_cnt <= wolf_cnt:
            return -1
        if max_sheep_cnt < sheep_cnt:
            # print(history)
            max_sheep_cnt = sheep_cnt
        if len(binary_tree[node]) == 2:
            first_node = binary_tree[node][0]
            second_node = binary_tree[node][1]
            if max_sheep_dict[first_node] != 0:
                if first_node not in history:
                    history.append(first_node)
                    dfs(first_node, sheep_cnt, wolf_cnt, access_list + [second_node], visited)
                    history.pop()

            if max_sheep_dict[second_node] != 0:
                if second_node not in history:
                    history.append(second_node)
                    dfs(second_node, sheep_cnt, wolf_cnt, access_list + [first_node], visited)
                    history.pop()

        elif len(binary_tree[node]) == 1:
            first_node = binary_tree[node][0]
            if max_sheep_dict[first_node] != 0:
                if first_node not in history:
                    history.append(first_node)
                    dfs(first_node, sheep_cnt, wolf_cnt, access_list, visited)
                    history.pop()

        for next_node in access_list:
            if max_sheep_dict[next_node] != 0:
                if next_node not in history:
                    history.append(next_node)
                    dfs(next_node, sheep_cnt, wolf_cnt, access_list + binary_tree[node], visited)
                    history.pop()
        # visited.pop()

    dfs(0, 0, 0, [], [])
    return max_sheep_cnt


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
