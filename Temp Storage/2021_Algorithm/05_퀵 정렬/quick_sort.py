# left, right를 안하고 0을 쓴다거나 mid 대신 p를 쓴다거나
# mid를 포함하는 실수함

from typing import List
import random



def choose_pivot(arr: List[int], left, right):
	return random.randrange(left, right + 1)

def partition(arr: List[int], left, right):
	p = arr[left]
	i = left + 1
	for j in range(left + 1, right + 1):
		if arr[j] < p:
			arr[j], arr[i] = arr[i], arr[j]
			i += 1
	arr[left], arr[i - 1] = arr[i - 1], arr[left]
	return i - 1

def quick_sort(arr: List[int], left, right) -> List[int]:
	if left >= right:
		return arr
	p = choose_pivot(arr, left, right)
	arr[left], arr[p] = arr[p], arr[left]
	mid = partition(arr, left, right)
	quick_sort(arr, left, mid -1)
	quick_sort(arr, mid + 1, right)
	return arr


T = int(input())
for _ in range(T):
	N = int(input())
	nums = list(map(int, input().split()))
	print(' '.join(map(str, quick_sort(nums, 0, len(nums) - 1))))
