
def kmp(text, pattern):
    ans = []
    pi = get_pi(pattern)
    n = len(text)
    m = len(pattern)
    j = 0
    for i in range(0, n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j -1]
        if text[i] == pattern[j]:
            if j == m - 1:
                ans.append(i - m + 1 + 1) # 답지 인덱스가 1개 많아서 + 1해줌
                j = pi[j]
            else:
                j += 1
    return ans

def get_pi(pattern):
    m = len(pattern)
    j = 0
    pi = [0 for _ in range(m)]
    for i in range(1 , m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    return pi


N = int(input())
for _ in range(N):
    res = kmp(*list(input().split()))
    print(len(res))
    if res:
        print(" ".join(map(str, res)))


