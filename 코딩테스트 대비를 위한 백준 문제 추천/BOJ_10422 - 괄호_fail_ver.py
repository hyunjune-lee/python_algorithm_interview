# [0. 날짜]
# 2021.07.27(화요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def sol(L):
    if L % 2 == 1:
        return 0
    bracket_wrap = 0
    bracket_add = 1
    while L != 2:
        bracket_wrap, bracket_add = bracket_wrap + bracket_add, 2* bracket_wrap + bracket_add
        L -= 2
    return (bracket_wrap + bracket_add) % 1000000007


T = int(input())
for _ in range(T):
    print(sol(int(input())))


# 2
# ()
# 4
# (())
# ()()

# dp[N] = bracket_wrap[N] + bracket_add[N]
# bracket_wrap[N] => bracket_wrap[N - 1] + bracket_add[N - 1]
# bracket_add[N] => 2 * bracket_wrap[N - 1] + bracket_add[N - 1]

# 감싸기 dp[N - 1] +
# ()추가 dp[N - 1] + dp[N - 1] - 1
# => 이전에 감싼거는 * 2
# 이전에 () 추가한거는 그대로 추가
# 6
# (()())
# ((()))

# ()()()
# (())()
# ()(()) 1

# 8
# 감싸기는 이전의 모든 것에 적용 가능
# ((()())) 2
# (()()()) 1
# (((()))) 2
# ((())()) 1
# (()(())) 1

# (()())()
# ()(()())
# ()()()()
# ()((()))
# ((()))()
# (())()()
# ()(())()


# ()붙이기는 대칭이 아닌 것엔 2배 => 2개
# 대칭이면 1개 => 3개
