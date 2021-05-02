# A번
T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    if len(set(nums)) != len(nums):
        print("true")
    else:
        print("false")
