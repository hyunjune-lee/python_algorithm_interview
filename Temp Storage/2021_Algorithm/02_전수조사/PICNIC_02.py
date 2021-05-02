# 2021-03-14
# 26분 22초

def dfs(idx):
	pair_count = 0
	if all(is_pair):
		return 1

	# 친구들을 돌면서 모두를 짝을 지어주는데
	# 중복이 안되게 짝의 뒤의 숫자가 앞보다 많을 수 없게 설정
	for i in range(idx, N - 1):
		for j in range(i + 1, N):
			if are_friend[i][j] and not is_pair[i] and not is_pair[j]:
				is_pair[i] = is_pair[j] = True
				pair_count += dfs(i + 1)
				is_pair[i] = is_pair[j] = False
	return pair_count

T = int(input())
for _ in range(T):
	# 값 입력받기
	N, M = map(int, input().split())
	friend_info  = list(map(int, input().split()))

	# 친구인지 판별하는 2차원 리스트
	are_friend = [[False for i in range(N)] for j in range(N)]

	# 친구 판별 2차원 리스트 채워넣기
	for i in range(M):
		a = friend_info[2 * i]
		b = friend_info[2 * i + 1]
		are_friend[a][b] = are_friend[b][a] = True

	is_pair = [False for x in range(N)]

	print(dfs(0))
