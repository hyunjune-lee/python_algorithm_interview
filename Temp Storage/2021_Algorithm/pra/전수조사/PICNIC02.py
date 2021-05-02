from collections import defaultdict


def match_dfs(pair_dict, pair_check):
    if all(pair_check):
        return 1
    ret = 0
    first_solo = pair_check.index(False)

    for pair_with in range(first_solo + 1, n):
        if first_solo in pair_dict[pair_with] and not pair_check[first_solo] and not pair_check[pair_with]:
            pair_check[first_solo] = pair_check[pair_with] = True
            ret += match_dfs(pair_dict, pair_check)
            pair_check[first_solo] = pair_check[pair_with] = False
    return ret


def pair_match(pairs, n):
    pair_dict = defaultdict(set)
    for a, b in pairs:
        pair_dict[a].add(b)
        pair_dict[b].add(a)
    pair_check = [False for _ in range(n)]

    return match_dfs(pair_dict, pair_check)


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())  # n 학생의 수, m : 친구쌍의 수
    input_friends = list(map(int, input().split()))
    pairs = list(zip(input_friends[::2], input_friends[1::2]))
    print(pair_match(pairs, n))
