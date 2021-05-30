def longest_substr(gap_penalty, mismatch_penalty, x, y):
    m = len(x)
    n = len(y)
    a = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match_penalty = -1 if x[i - 1] == y[j - 1] else mismatch_penalty
            a[i][j] = min(a[i - 1][j - 1] + match_penalty, a[i - 1][j] + gap_penalty, a[i][j - 1] + gap_penalty)
    return a[m][n]


T = int(input())
for _ in range(T):
    X = input()
    Y = input()
    print(abs(longest_substr(0, 0, X, Y)))
