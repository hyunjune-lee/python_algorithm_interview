# Dynamic Programming

## 전수조사(트리), 메모이제이션, 테뷸레이션 차이

```py
coutn_sum 목표 정수 m, n개의 정수
# 트리로 표현

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

## 메모이제이션 접근 방법

1. 항상 기저 사례를 제일 먼저 처리

## 점화식 구하기

- 지금 요소가 포함되냐 안되냐
  - 마지막 값이 최종해에 포함될 수 있고 포함되지 않을 수 있음 포함되면 어떤 의미? 포함되지 않으면 어떤 의미?
- 최적해의 구조, 특성을 통해 유추
- 거기서 갈라지는 경우의 수 중에서 최적을 찾는 경우를 생각하기
- 최적해는 부분합의 최적해가 되어야 동적프로그래밍이 가능하다.

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
