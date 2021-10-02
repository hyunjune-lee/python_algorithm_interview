def power_count(goal, num):
    ret = 1
    cnt = 0
    while ret <= goal:
        ret *= num
        cnt += 1


    return cnt -1


T = int(input())

for _ in range(T):
    n = int(input())
    print(min(power_count(n, 2),power_count(n, 5)))