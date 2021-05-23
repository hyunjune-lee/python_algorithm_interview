# f_sum의 원리는 다 1씩 빼주기 떄문에 그게 모여서 세트가 되는군


def optimal_bst(key_count, f):
    c = [[0 for _ in range(key_count + 2)] for _ in range(key_count + 2)]
    for i in range(1, key_count + 2):
        c[i][i - 1] = 0
    for size in range(key_count):
        for i in range(1, key_count - size + 1):
            f_sum = sum(f[k - 1] for k in range(i, i + size + 1))
            min_subset = float("inf")
            for r in range(i, i + size + 1):
                min_subset = min(min_subset, c[i][r - 1] + c[r + 1][i + size])
            c[i][i + size] = f_sum + min_subset
    return c[1][key_count]


T = int(input())
for _ in range(T):
    N = int(input())  # 키의 개수
    F = list(map(int, input().split()))  # 검색 빈도
    print(optimal_bst(N, F))

    # for line in a:
    #     print(line)
    # print("------------------")
