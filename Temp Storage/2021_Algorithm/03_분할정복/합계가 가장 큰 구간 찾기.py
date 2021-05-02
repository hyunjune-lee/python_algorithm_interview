from typing import List


def dc_find_maximum_subarray(arr: List[int]):
    if len(arr) == 1:
        return arr[0]

    m = (len(arr)) // 2

    left_max_sum = dc_find_maximum_subarray(arr[:m])
    right_max_sum = dc_find_maximum_subarray(arr[m:])

    # 중간(미포함)에서 왼쪽으로 진행했을 때의 최대 합계
    left_sum = mid_to_left_max_sum = 0
    for left_idx in range(m - 1, -1, -1):
        left_sum += arr[left_idx]
        mid_to_left_max_sum = max(left_sum, mid_to_left_max_sum)

    # 중간(포함)에서 오른쪽으로 진행했을 때의 최대 합계
    right_sum = mid_to_right_max_sum = 0
    for right_idx in range(m, len(arr)):
        right_sum += arr[right_idx]
        mid_to_right_max_sum = max(right_sum, mid_to_right_max_sum)

    # 왼쪽, 오른쪽에서의 최대값과 가운데서 좌우로 진행했을 떄의 최대값 중 큰 값이 전체에서 큰 값
    return max(max(left_max_sum, right_max_sum), mid_to_left_max_sum + mid_to_right_max_sum)


T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    print(dc_find_maximum_subarray(nums))
