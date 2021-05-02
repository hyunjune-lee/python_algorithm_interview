# 20분 걸림
def dfs(gap_to_target):
	global is_cansum

	for i in range(N):
		gap = gap_to_target - X_list[i]
		if gap > 0:
			dfs(gap)
		elif gap == 0 :
			is_cansum = True
			return

T = int(input())
for _ in range(T):
	M, N = list(map(int, input().split()))
	X_list = list(map(int, input().split()))
	is_cansum = False
	dfs(M)
	print("true" if is_cansum else 'false' )
