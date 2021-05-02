def find_best_sum(gap_to_target):
    global best_sum
    if gap_to_target < 0:
        return
    elif gap_to_target == 0:
        best_sum.append(now_sum[:])
        return

    for num in nums:
        now_sum.append(num)
        find_best_sum(gap_to_target - num)
        now_sum.pop()


for _ in range(int(input())):
    M, N = map(int, input().split())
    nums = list(map(int, input().split()))
    now_sum = []
    best_sum = []
    find_best_sum(M)
    best_sum.sort(key=len)
    if not best_sum:
        print(-1)
    else:
        print(len(best_sum[0]), " ".join(map(str, best_sum[0])))
