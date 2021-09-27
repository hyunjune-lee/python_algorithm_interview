# [0. 날짜]
# 2021.09.27(월요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# => 답지 참고
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기] 

import sys
input = sys.stdin.readline

n, B = 2, int(input())
A = [[1,1],[1,0]]

def power(a,b,n):
    cal = []
    for i in range(n):
        temp = []
        for j in range(n):
            num = 0
            for k in range(n):
                num += a[i][k] * b[k][j]
            temp.append(num%1000000007)
        cal.append(temp)
    return cal
    # 행렬의 곱셉을 함수화 해보았다.

def dac(s,b):
    if b == 1:
        return s
    
    a = dac(s,b//2)
    
    cal = power(a,a,n)
    
    result = []
    if b % 2:
        result = power(cal,A,n)
    else:
        result = cal
        
    return result
print(dac(A,B)[0][1])