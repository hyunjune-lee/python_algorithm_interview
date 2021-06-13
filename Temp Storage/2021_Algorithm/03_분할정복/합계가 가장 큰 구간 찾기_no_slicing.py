# [주의] //연산이 소수점 아래를 버리기 때문에
# 주석 처리된 right_max_sum에서 m , h 인 경우에
# 다음 m이 (2+3)//2 => 2로 m,h가 또 2, 3이 된다
# 즉 무한루프를 돌 수 있다.
# 만약 바뀐 left_max_sum에 l, m 에 2, 3이 들어오면
# m = (2 + 3)//2 => 2으로 l, m 은 2, 2가 된다. 즉 무한 루프(X)
# left_max_sum = dc_find_maximum_subarray(arr, l, m - 1)
# right_max_sum = dc_find_maximum_subarray(arr, m, h)

from typing import List


def dc_find_maximum_subarray(arr: List[int], l, h):
	# 배열의 개수가 1개 일때
	if h <= l:
		return arr[h]

	m = (l + h)//2


	# 중간(미포함)에서 왼쪽으로 진행했을 때의 최대 합계
	left_sum = mid_to_left_max_sum = 0
	for left_idx in range(m - 1, l - 1, -1):
		left_sum += arr[left_idx]
		mid_to_left_max_sum = max(left_sum, mid_to_left_max_sum)

	# 중간(포함)에서 오른쪽으로 진행했을 때의 최대 합계
	right_sum = mid_to_right_max_sum = 0
	for right_idx in range(m, h + 1):
		right_sum += arr[right_idx]
		mid_to_right_max_sum = max(right_sum, mid_to_right_max_sum)

	left_max_sum = dc_find_maximum_subarray(arr, l, m)
	right_max_sum = dc_find_maximum_subarray(arr, m + 1, h)

	# 왼쪽, 오른쪽에서의 최대값과 가운데서 좌우로 진행했을 떄의 최대값 중 큰 값이 전체에서 큰 값
	return max(max(left_max_sum, right_max_sum), mid_to_left_max_sum + mid_to_right_max_sum )


T = int(input())
for _ in range(T):
	N = int(input())
	nums = list(map(int, input().split()))
	print(dc_find_maximum_subarray(nums, 0, len(nums) - 1))
