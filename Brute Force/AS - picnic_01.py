# ---------------------------------------------
# 책 참고한 코드


def count_pairings(taken):
    first_free = -1
    for i in range(n):
        if not taken[i]:
            first_free = i
            break

    if first_free == -1:
        return 1
    ret = 0
    for pair_with in range(first_free + 1, n):
        if not taken[pair_with] and areFriends[first_free][pair_with]:
            taken[first_free] = taken[pair_with] = True
            ret += count_pairings(taken)
            taken[first_free] = taken[pair_with] = False
    return ret


C = int(input())

for _ in range(C):
    n, m = map(int, input().split())
    areFriends = [[False for col in range(10)] for row in range(10)]
    taken = [False for j in range(10)]
    partner = list(map(int, input().split()))
    for i in range(0, len(partner), 2):
        areFriends[partner[i]][partner[i + 1]] = True
        areFriends[partner[i + 1]][partner[i]] = True
    print(count_pairings(taken))

# ---------------------------------------------------
# 다른 사람 코드


def process(selected, ni):
    global answer
    if selected == n:
        answer = answer + 1
        return

    for i in range(ni, len(pairs)):
        f, s = pairs[i]
        if flags[f] == 0 and flags[s] == 0:
            flags[f], flags[s] = 1, 1
            process(selected + 2, i + 1)
            flags[f], flags[s] = 0, 0


c = int(input())
for _ in range(c):
    n, m = map(int, input().split())
    elems = list(map(int, input().split()))
    pairs = list(zip(elems[::2], elems[1::2]))

    answer, flags = 0, [0] * n
    process(0, 0)
    print(answer)
# ------------------
# 개선된 코드
