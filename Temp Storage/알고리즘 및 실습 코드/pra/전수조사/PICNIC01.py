from collections import defaultdict


def match_dfs(pair_dict, pair_check, ret, start):
    if all(pair_check):
        return 1

    for i in range(start, n - 1):
        for j in range(i + 1, n):
            if i in pair_dict[j] and not pair_check[i] and not pair_check[j]:
                pair_check[i] = pair_check[j] = True
                ret += match_dfs(pair_dict, pair_check, 0, i + 1)
                pair_check[i] = pair_check[j] = False
    return ret


def pair_match(pairs, n):
    pair_dict = defaultdict(set)
    for a, b in pairs:
        pair_dict[a].add(b)
        pair_dict[b].add(a)
    pair_check = [False for _ in range(n)]

    return match_dfs(pair_dict, pair_check, 0, 0)


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())  # n 학생의 수, m : 친구쌍의 수
    input_friends = list(map(int, input().split()))
    pairs = list(zip(input_friends[::2], input_friends[1::2]))
    print(pair_match(pairs, n))
