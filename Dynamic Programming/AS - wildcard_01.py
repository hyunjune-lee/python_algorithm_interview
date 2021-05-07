def wildcard_check(W, files):



T = int(input())
for _ in range(T):
    W = input()
    N = int(input())
    files = []
    for i in range(N):
        files.append(input())
    wildcard_check(W, files)
