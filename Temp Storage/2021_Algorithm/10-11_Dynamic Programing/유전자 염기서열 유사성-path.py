# 처음에 배열 만들때 x,y 축 반대로함(다음엔 x,y 축 다른 케이스 체크하기)


def gene_similarity(gap_penalty, mismatch_penalty, x, y):
    m = len(x)
    n = len(y)
    a = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    path = [[[] for _ in range(n + 1)] for _ in range(m + 1)]
    path[0][0] = [(0, 0)]
    for i in range(1, m + 1):
        a[i][0] = i * gap_penalty
        path[i][0] = [(i, 0)] + path[i - 1][0]
    for j in range(1, n + 1):
        a[0][j] = j * gap_penalty
        path[0][j] = [(0, j)] + path[0][j - 1]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match_penalty = 0 if x[i - 1] == y[j - 1] else mismatch_penalty
            a[i][j] = min(a[i - 1][j - 1] + match_penalty, a[i - 1][j] + gap_penalty, a[i][j - 1] + gap_penalty)
            if a[i][j] == a[i - 1][j - 1] + match_penalty:
                path[i][j] = [(i, j)] + path[i - 1][j - 1]
            elif a[i][j] == a[i - 1][j] + gap_penalty:
                path[i][j] = [(i, j)] + path[i - 1][j]
            elif a[i][j] == a[i][j - 1] + gap_penalty:
                path[i][j] = [(i, j)] + path[i][j - 1]
    print(path[m][n])
    return a[m][n]


T = int(input())
for _ in range(T):
    G, M, X, Y = input().split()
    print(gene_similarity(int(G), int(M), X, Y))

    # for line in a:
    #     print(line)
    # print("------------------")
