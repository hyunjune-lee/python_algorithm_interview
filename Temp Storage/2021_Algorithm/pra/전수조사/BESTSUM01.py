# not best_sum 대신에서 best_sum is None으로 검사하니 된다..
import random


def find_best_sum(gap_to_target):
    global best_sum
    if gap_to_target < 0:
        return
    elif gap_to_target == 0:
        if best_sum is None or len(now_sum) < len(best_sum):
            best_sum = now_sum[:]
        return

    for num in nums:
        now_sum.append(num)
        find_best_sum(gap_to_target - num)
        now_sum.pop()


for _ in range(int(input())):
    M, N = map(int, input().split())
    nums = list(map(int, input().split()))
    now_sum = []
    best_sum = None
    find_best_sum(M)
    if best_sum is None:
        print(-1)
    else:
        print(len(best_sum), " ".join(map(str, best_sum)))
    print([1, 2][False])
