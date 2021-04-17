# 리턴으로 구현하는 방법 없을까?
def dfs(gap_to_target):

	for i in range(N):
		gap = gap_to_target - X_list[i]
		if gap > 0:
			dfs(gap)
		elif gap == 0 :
			return True
	return False



T = int(input())
for _ in range(T):
	M, N = list(map(int, input().split()))
	X_list = list(map(int, input().split()))

	print("true" if dfs(M) else 'false' )
