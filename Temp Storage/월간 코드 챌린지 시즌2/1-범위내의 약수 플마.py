import math

# 제곱근까지만 진행, 제곱근이 정수이면 + 1 그전에는 2개씩
def solution(left, right):
    sum = 0
    for num in range(left, right + 1):
        # print(num, math.ceil(math.sqrt(num)))
        count = 0
        for check_num in range(1, math.ceil(math.sqrt(num))):
            if num % check_num == 0:
                count += 2
        if int(math.sqrt(num)) == math.sqrt(num):
            count += 1
        if count % 2 == 0:
            sum += num
        else:
            sum -= num

    return sum


print(solution(13, 17))
print(solution(24, 27))
