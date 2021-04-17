from typing import List
import random

def partition(arr: List[int], left, right):
	pivot_i = random.randrange(left, right+ 1)
	arr[left], arr[pivot_i] = arr[pivot_i], arr[left]
	pivot = arr[left]

	i = left + 1
	for j in range(left + 1, right + 1):
		if arr[j] < pivot:
			arr[j], arr[i] = arr[i], arr[j]
			i += 1
	arr[left], arr[i - 1] = arr[i - 1], arr[left]
	return i - 1

def r_select(arr, left, right, k) -> int:
	if left == right:
		return arr[left]

	mid = partition(arr, left, right)
	if mid == k -1: # 배열의 인덱스때문에 1차이
		return arr[mid]
	elif mid > k - 1:
		return r_select(arr, left, mid - 1, k)
	else:
		return r_select(arr, mid + 1, right, k)


T = int(input())
for _ in range(T):
	N, k = list(map(int, input().split()))
	nums = list(map(int, input().split()))
	print(r_select(nums, 0, N - 1, k))
