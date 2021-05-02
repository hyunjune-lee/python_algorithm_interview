from typing import List
import sys


def optimal_find_second_max(nums: List[int], n: int) -> List[int]:
    if n == 2:
        return nums[0] if nums[0] < nums[1] else nums[1]
    # 2n - 1 크기 리스트 준비
    heap = [0 for _ in range(2 * n - 1)]
    # n - 1 위치부터 원래 값을 저장
    for i, num in enumerate(nums):
        heap[n - 1 + i] = num
    # 뒤에서 부터 토너먼트 진행
    for i in range(2 * n - 2, 1, -2):
        heap[i // 2 - 1] = heap[i] if heap[i - 1] < heap[i] else heap[i - 1]

    # [FIX] 0 =>  -(sys.maxsize + 1)
    second_max = -(sys.maxsize + 1)
    i = 1
    # 토너먼트 올라가면서 상대들 비교하기
    while i < 2 * n - 1:
        # heap[i]가 최댓값의 비교 상대라면
        if heap[i] < heap[0]:
            second_max = max(heap[i], second_max)
            i = i + 1
        else:  # heap[i + 1]가 최댓값의 비교 상대라면
            second_max = max(heap[i + 1], second_max)
        i = 2 * i + 1

    return second_max


T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    print(optimal_find_second_max(nums, N))
