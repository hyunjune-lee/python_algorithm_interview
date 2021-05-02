def dfs(gap_to_target):
	count = 0
	if gap_to_target == 0:
		ret_list.append(path[:])
		return 1

	for i in range(N):
		gap = gap_to_target - X_list[i]
		if gap >= 0:
			path.append(X_list[i])
			count += dfs(gap)
			path.pop()

	return count

T = int(input())
for _ in range(T):
	M, N = list(map(int, input().split()))
	X_list = list(map(int, input().split()))

	path = []
	ret_list = []
	dfs(M)

	if ret_list:
		print(len(ret_list[0]), " ".join(map(str, ret_list[0])))
	else:
		print(-1)
