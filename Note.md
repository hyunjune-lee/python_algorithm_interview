# 알고리즘 접근 순서

1. 기본적인 전수조사: 경우의 수가 제한적인 경우에만 사용 가능
   - 재귀 호출을 이용하여 구현
   - 종료조건, 조사 순서 중요(중복 답 제거 포함)
2. 특정 경우만 조사하여 답을 찾을 수 있으면 탐욕적 기법
3. 중복 계산이 많을 수 있음 -> 메모이제이션
4. 하향식이 아니라 상향식 -> 테뷸레이션
   - 점화식을 찾는 것이 핵심
5. 전수조사하지만 노드가 유망하지 않으면 배제 -> 되추적
   - 유망 여부를 검사할 수 있어야 함
   - DFS
6. 가장 유망한 노드부터 검사 -> 분기 한정

   - 우선 순위 큐 기반 BFS

7. 양에 따라서
8. 적으면 -> 전수조사
9. 많으면 -> 다이나믹 적용 여부
   2-1. 다이나믹 적용되면 다이나믹 프로그래밍
   2-2. 다이나믹 적용 안되면 백트래킹?

그리디, 다이나믹, 분할정복

## 알고리즘 접근 팁

1. 뭔가 충돌하거나 안에서부터 비교하는 거면 Stack 생각해보기

# 알고리즘 중요한 팁들

## lower bound

lower bound는 찾고자 하는 값 이상이 처음 나타나는 위치

```py
def binary_search(score_list, score):
    l, r = 0, len(score_list)
    while l < r:
        mid = (l + r) // 2
        if score <= score_list[mid] :
            r = mid
        else:
            l = mid + 1
    return


# 여기서 lower bound는 idx 1이다.(2가 제일 처음 나타나는 위치)
# 여기서 upper bound는 idx 4이다. (2 초과한 값이 처음 나타나는 위치)
print(binary_search([1, 2, 2, 2, 4, 8, 12], 2))
```

## Upper bound

lower bound는 찾고자 하는 값 이상이 처음으로 나타나는 위치인 반면에, upper bound는 찾고자 하는 값보다 큰 값이 처음으로 나타나는 위치입니다.
`if score < score_list[mid]` 에서 < 이면 upper bound, <= 이면 lower bound

```py
def binary_search(score_list, score):
    l, r = 0, len(score_list)
    while l < r:
        mid = (l + r) // 2
        if score < score_list[mid] :
            r = mid
        else:
            l = mid + 1
    return


print(binary_search([1, 2, 2, 2, 4, 8, 12], 2))
```

## 누적합에서 값 구하기..

카카오 광고시간, 튜플 문제에서..

# 알고리즘 소소한 팁들

## 1. eval를 사용하면 있는 그대로 활용할 수 있다.

```

# 패킹할때 매개변수 앞에 *을 붙여서 한다.
# Python 3.7 이상의 버전부터 dictionary는 "key"값을 넣는 순서를 기억한다. 따라서, dict을 이용해서 가장 간단한 방법으로 리스트의 중복을 제거하면서 기존 리스트의 순서를 유지할 수 있다. [6,7]

```

## 다중 조건으로 정렬하기

```
a = [(1, 2), (0, 1), (5, 1), (5, 2), (3, 0)]

# 인자없이 그냥 sorted()만 쓰면, 리스트 아이템의 각 요소 순서대로 정렬을 한다.

b = sorted(a)

# b = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

# key 인자에 함수를 넘겨주면 해당 함수의 반환값을 비교하여 순서대로 정렬한다.

c = sorted(a, key = lambda x : x[0])

# c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

d = sorted(a, key = lambda x : x[1])

# d = [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]

# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,

# 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다.

e = [(1, 3), (0, 3), (1, 4), (1, 5), (0, 1), (2, 4)]
f = sorted(e, key = lambda x : (x[0], -x[1]))

# f = [(0, 3), (0, 1), (1, 5), (1, 4), (1, 3), (2, 4)]

출처 : https://dailyheumsi.tistory.com/67
```

## 파이썬 중복 제거

# 자주 하는 실수

1. 범위 한끗차이

```
range(m - 1), range(m)
```

2. x,y 축 헷갈림

```
a = [[0 for i in range(n + 1)] for j in range(m + 1)] =>
a = [[0 for i in range(m + 1)] for j in range(n + 1)]
```

3. None인식 헷갈림

```
if res => if res is not None:
```

```

```
