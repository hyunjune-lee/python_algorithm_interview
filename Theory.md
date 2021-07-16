# 01. 빅O

빅O는 입력 크기가 매우 클 때만 유용함
빅O는 점근적 최악의 경우에 대한 분석임
해결해야 하는 문제에서 입력 크기의 범위를 주의 깊게 살펴보자.
소수 판별처럼 입력 크기를 고려할 때 주의해야 하는 문제들이 있음

## 빅 오 => 같거나 좋음

## 빅 오메가 => 같거나 나쁨

# kmp: 문자열 검색 알고리즘

[kmp: 문자열 검색 알고리즘 설명 블로그](https://bowbowbow.tistory.com/6)

```py


def kmp(text, pattern):
    ans = []
    pi = get_pi(pattern)
    n = len(text)
    m = len(pattern)
    j = 0
    for i in range(0, n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]
        if text[i] == pattern[j]:
            if j == m - 1: # pattern이 모두 일치하면
                ans.append(i - m + 1)
                j = pi[j] # 다시 떙겨서 검사 이때는 현재위치까지도 일치하기 때문에 j- 1이 아닌 j
            else:
                j += 1
    return ans


#         while j > 0 and p[i] != p[j]:
#            j = pi[j - 1]
# j > 0 이 없으면 무한 반복.. 이 파트가 j를 뛰어넘는 파트인데 0에서 또 뛰어넘을 필요 없잖아
# p[i] != p[j] => 지금 단어가 맞지 않으니
# j = pi[j - 1] => 이전(j - 1)까지 일치한 만큼 땡겨서 다시 검색하라
# pi[j -1]이 만약 6이면 6자리가 일치한다는 뜻이다.
# 근데 index가 0부터 시작하기 때문에 6이면 6자리 일치한 직후의 index이기 때문에
# 그 index부터 검사해도 좋다.


def get_pi(pattern):
    m = len(pattern)
    j = 0
    pi = [0 for _ in range(m)]
    for i in range(1, m):  # i가 0 이면 한글자짜리 부분 문자열이다. 그래서 1부터 시작한다.
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    return pi

```
