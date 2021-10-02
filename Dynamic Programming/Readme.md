# Dynamic Programming

## 유형

### 한쪽 방향으로 진행(카데인 알고리즘)

BOJ_15486 - 퇴사 2.py

```py
def solution():
    for i in range(1, N + 1):
        take_time, amount = counseling_list[i - 1]
        # 오늘의 금액이 전날의 금액이 큰지, 아니면 전에 일하다 오늘 마친후의 금액이 큰지?
        dp_amount[i] = max(dp_amount[i - 1], dp_amount[i])
        # 오늘 일했을 때의 다음 날의 금액
        if i + take_time < N + 2:
            dp_amount[i + take_time] = max(dp_amount[i + take_time], dp_amount[i] + amount)
    dp_amount[N + 1] = max(dp_amount[N], dp_amount[N + 1])
    return dp_amount[N + 1]
```

### 앞뒤 분할 정복 메모이제이션

BOJ_11049 - 행렬 곱셈 순서.py


```py
# memo[s][e] = s번째 행렬부터 e번째 행렬까지의 곱센 연산의 최솟값이라 해보자
# memo[s][e] = memo[s][i] + memo[i + 1][e] + mat[s][0]*mat[i][1] * mat[e][1]
def sol(s, e):
    if memo[s][e]:
        return memo[s][e]
    if e - s == 1:
        memo[s][e] = mats[s][0] * mats[s][1] * mats[e][1]
        return memo[s][e]
    if s == e:
        return 0
    ret = 0
    for i in range(s, e):
        ret = sol(s, i) + sol(i + 1, e) + mats[s][0] * mats[i][1] * mats[e][1]
        if not memo[s][e] or ret <memo[s][e]:
            memo[s][e] = ret

    return memo[s][e]
```

### 상태에 따른 메모이제이션

BOJ_12996 - Acka.py
```py
# n번째 곡에서 a,b,c 상태가 똑같다면 그 뒤에 나오는 케이스도 똑같기 때문에
# 메모이제이션을 통해 기록하고 이미 구한 상태라면 넘긴다.
def sol(n, a, b, c):
    if n == S:
        if a + b + c == 0:
            return 1
        return 0
    if memo[n][a][b][c] >= 0:
        return memo[n][a][b][c]

    memo[n][a][b][c] = 0
    for delta_a, delta_b, delta_c in [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (1, 0, 1), (0, 1, 1), (1, 1, 1)]:
        na, nb, nc = a - delta_a, b - delta_b, c - delta_c
        if na < 0 or nb < 0 or nc < 0:
            continue
        memo[n][a][b][c] += sol(n + 1, na, nb, nc)
    memo[n][a][b][c] %= 1000000007
    return memo[n][a][b][c]


S, a, b, c = map(int, input().split())
memo = [[[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

print(sol(0, a, b, c))

```

BOJ_14238 - 출근 기록.py
```py
# memo = [전전날][전날][오늘 남은 A 출근날][오늘 남은 B 출근날][오늘 남은 C 출근날]
from collections import defaultdict


def abc_to_int(char):
    if char == "A":
        return 1
    elif char == "B":
        return 2
    elif char == "C":
        return 3
    elif char == " ":
        return 0


def sol(n):
    if n - 2 == len(input_remain):
        return 1
    memo_res = memo[abc_to_int(work_record[n - 2])][abc_to_int(work_record[n - 1])][abc[1]][abc[2]][abc[3]]
    if memo_res:
        return 0
    memo[abc_to_int(work_record[n - 2])][abc_to_int(work_record[n - 1])][abc[1]][abc[2]][abc[3]] = 1
    for i, staff in enumerate("ABC"):
        if abc[i + 1] > 0 and dp[n][i]:
            for j in range(i):
                dp[n + j + 1][i] = False
            work_record.append(staff)
            abc[i + 1] -= 1
            if sol(n + 1):
                return 1
            for j in range(i):
                dp[n + j + 1][i] = True
            abc[i + 1] += 1
            work_record.pop()

    return 0


dp = [[True, True, True] for _ in range(55)]
memo = [[[[[0 for _ in range(55)] for _ in range(55)] for _ in range(55)] for _ in range(4)] for _ in range(4)]
input_remain = list(input())
abc = [0, 0, 0, 0]
for c in input_remain:
    num = abc_to_int(c)
    abc[num] += 1

work_record = [" ", " "]
if sol(2):
    print("".join(work_record[2:]))
else:
    print(-1)
```


## TIP

### 한쪽 방향으로만 진행하게 하는 것

#### 2차원일때 BOJ 점프에서

```py
# 가는 방향이 고정되어있으므로 맨위쪽위부터 오른쪽으로,
# 그리고 아래 줄 이렇게 진행해서 진행 경로의 수가 적힌 dp_board를 만나면
# 해당 경로에서 그 숫자만큼 오른쪽, 아래에 dp_board 에 현재 적힌 경로의 수 만큼 더해준다.
for y in range(N):
    for x in range(N):
        if dp_board[y][x] and board[y][x]:
            jump_dist = board[y][x]
            # 오른쪽
            if x + jump_dist < N:
                dp_board[y][x + jump_dist] += dp_board[y][x]
            # 아래쪽
            if y + jump_dist < N:
                dp_board[y + jump_dist][x] += dp_board[y][x]
return dp_board[N - 1][N - 1]

```

#### 중복 안되게 더할 떄

BOJ_15989 - 1, 2, 3 더하기 4_2.py
1를 먼저 쭉 더하고, 2 쭉 더하고, 3쭉 더하는 식

```py
def solution(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1

    for add_num in [1, 2, 3]:
        for x in range(add_num, n + 1):
            dp[x] += dp[x - add_num]
    return dp[n]
```

## 전수조사(트리), 메모이제이션, 테뷸레이션 차이

```py

coutn_sum 목표 정수 m, n개의 정수
# 전수조사(트리로 표현)

시간 복잡도 : O(n^m)
공간 복잡도 : O(m + n)
canSum(m, nums)
    if m<0 then return false
    if m==0 then return true
    for x in nums do
        if canSum(m-x, nums) then return true
    return false

# 메모이제이션
시간 복잡도 : O(mm)
공간 복잡도 : O(3m + n)
canSum(m, nums, memo)
    if m<0 then return false
    if m==0 then return true
    if m in memo then return memo.get(n)
    for x in nums do
        if canSum(m-x, nums) then
            memo.set(m, true)
            return true
    memo.set(m, false)
    return false

# 테뷸레이션
시간 복잡도 : O(mm)
공간 복잡도 : O(n)
canSum(m, nums)
    table = [] // size m+1
    table[0] = true
    for i=0 to m-1 do
        if table[i] then
            for x in nums
                if i+x<=m then table[i+x] = true
    return table[m]

}
```

## 동적 프로그래밍 설계 방법의 3가지 단계 (테뷸레이션)

단계 1. 부분 문제 식별하기
단계 2. 작은 문제의 해로부터 큰 문제의 해를 구하는 효율적 방법 찾기
단계 3. 모든 부분 문제의 해로부터 원 문제의 해를 구하는 효율적 방법 찾기
또 다른 방법: 전수조사 방법을 구현한 다음 메모이제이션 적용

단계 1에서는 부분 문제의 수가 중요함: 성능을 결정함
단계 2는 점화식 찾기
부분 문제를 식별하는 것과 점화식을 구하는 것은 훈련이 필요함!!!

피보나치 문제의 예
단계 1: n − 1개의 부분 문제를 해결해야 함. f(2), f(3), ..., f(n)
단계 2: f(n) = f(n − 1) + f(n − 2)
문제에 주어진 식임. 하지만 다른 문제는 이 식을 찾는게 어려울 수 있음
단계 3: 가장 큰 부분 문제의 해가 원 문제의 해임

## 메모이제이션 접근 방법

1. 항상 기저 사례를 제일 먼저 처리

## 점화식 구하기

- 지금 요소가 포함되냐 안되냐
  - 마지막 값이 최종해에 포함될 수 있고 포함되지 않을 수 있음 포함되면 어떤 의미? 포함되지 않으면 어떤 의미?
- 최적해의 구조, 특성을 통해 유추
- 거기서 갈라지는 경우의 수 중에서 최적을 찾는 경우를 생각하기
- 최적해는 부분합의 최적해가 되어야 동적프로그래밍이 가능하다.

## 분할정복과 동적프로그래밍 비교

차이점 1. 분할 정복은 분할한 것을 결합하여 해를 구하는 반면에 동적 프로그래밍은 분할 것 중 하나를 선택함

차이점 2. 분할 정복의 재귀 호출은 보통 중복되지 않음

차이점 3. 분할 정복은 직관적인 다항 시간 알고리즘의 성능을 개선함.
<br>동적 프로그래밍은 직관적인 지수 시간 알고리즘을 다항 시간으로 개선함

차이점 4. 분할 정복은 성능을 개선하기 위해 부분 문제를 선택함. 동적 프로그래밍은 답을 찾기 위해 부분 문제를 선택함 빠른 정렬은 어떤 피봇을 선택하여도 올바르게 정렬함

차이점 5. 분할 정복은 부분 문제의 크기가 상수 비율로 축소되지만
동적 프로그래밍은 그렇지 않을 수 있음
WIS는 n에서 n − 1

## 최적화 문제

- 최적화 문제(optimization problem) 가능한 모든 해로부터 가장 최적의 해를 찾는 문제
- 최적 원칙(principle of optimality)이 만족되면 최적화 문제는 동적 프로그래밍으로 프로그래밍 가능

### 최적 원칙

어떤 문제의 사례에 대한 최적해가 그 사례의 부분 사례의 최적해를 항상 포함하고 있으면 이 원칙이 적용되는 문제임

- 예) 최단 경로 문제: 최적 원칙 적용 가능 문제
- 예) 최장 경로 문제: 최적 원칙 적용이 가능하지 않은 문제
- 노드 1에서 4까지의 최장 경로 [1,3,2,4] = 7
- 노드 1에서 3까지의 최장 경로 [1,2,3] = 4

## 대표 문제 - 최단 경로 찾기 문제

- 경로 길이가 최대 n − 1인 것 까지만 고려함
  - n - 1보다 큰 길이의 경로는 그보다 항상 짧은 길이의 경로를 만들 수 있음
    - n - 1보다 크면 한 노드 w를 두 번 이상 방문하는 것을 의미함 경로에 주기가 존재한다는 것임
    - 이 주기를 제거하면 더 짧은 경로를 확보할 수 있음

### Bellman-Ford

- 시간복잡도 O(mn) 여기서 m이 n^2정도 됨
- 음의 주기 있으면(체크해줌)

### Floyd-Warshall

- 시간복잡도 O(n^3) (모든 쌍에 대해서 구해주기 때문에 Bellman-Ford알고리즘을 n번 호출하는 것보다 효율적임)
- 음의 주기가 있으면 안됨(그래도 음의 주기를 체크해주긴함)
- k i j 순서 중요!!! (i j k 순서로 하면 제대로 안됨)

```py
def find_shortest_path_by_floyd(n, mat):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if mat[i][j] > mat[i][k] + mat[k][j]:
                    mat[i][j] = mat[i][k] + mat[k][j]
                    table[i][j] = k
```
