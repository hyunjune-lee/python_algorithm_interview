# B번
T = int(input())
for _ in range(T):
	# 이전 코드에서 입력 후에 슬라이싱하던 것을 바로 unpacking하여 시간, 공간 개선
	N, *nums = list(map(int, input().split()))

	nums.sort() # n logn

	max_appear = 0
	appear_count = 1
	before_n = -1
	max_n = -1

	for n in nums:
		if before_n != n:
			appear_count = 1
			before_n = n
		else:
			appear_count += 1

		if appear_count > max_appear:
			max_appear = appear_count
			max_n = n
	print(max_n)
