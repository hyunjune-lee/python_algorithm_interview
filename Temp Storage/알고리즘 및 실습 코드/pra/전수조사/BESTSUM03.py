def find_best_sum(gap_to_target):
    if gap_to_target < 0:
        return None
    elif gap_to_target == 0:
        return []
    best = []
    for num in nums:
        find_sum = find_best_sum(gap_to_target - num)
        if find_sum is not None:
            if not best or len(best) > len(find_sum) + 1:
                find_sum.append(num)
                best = find_sum
    return best


for _ in range(int(input())):
    M, N = map(int, input().split())
    nums = list(map(int, input().split()))

    best_sum = find_best_sum(M)
    if not best_sum:
        print(-1)
    else:
        print(len(best_sum), " ".join(map(str, best_sum)))
