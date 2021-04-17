# 2시간 10분 걸림

# 블록 => 중복 방지를 위해서  ㄴ, 좌우로 뒤집어진 ㄴ, ㄱ, 좌우로 뒤집어진 ㄱ 의 블록만 사용한다.
# [!] - 좌우로 뒤집어진 ㄱ 생각 못함ㅠ
block_case = [
			[(0,0), (1, 0), (1, 1)],
			[(0,0), (1, 0), (1, -1)],
			[(0,0), (0, 1), (1, 1)],
			[(0, 0), (1, 0), (0, 1)]
			]


def is_block_ok(y, x, block) -> bool:
	for my, mx in block:
		if not(0 <= y + my < H and 0 <= x + mx < W):
			return False
		if board[y + my][x + mx] == '#':
			return False
	return True

def block_convert(y, x, block, paint):
	for my, mx in block:
		board[y + my][x + mx] = paint

# 1.여기서 괜히 range(sx, W)로 범위 제한해서 제대로 동작 안함
# 2. for문안에 dfs가 있으면 계속 중복이 생겨서 이 메소드 만듬
# => 제일 처음 열린 부분을 찾아서 거기서부터 dfs 함
def find_first_open_board():
	for y in range(H):
		for x in range(W):
			if board[y][x] == '.':
				return [y,x]
	return [-1, -1]

def open_board_counter():
	count = 0
	for line in board:
		for x in line:
			if x == '.':
				count += 1
	return count

def dfs(left_board):
	board_cover_count = 0
	if left_board == 0:
		return 1

	y, x = find_first_open_board()
	for block in block_case:
		if is_block_ok(y, x, block):
			block_convert(y, x, block, '#')
			board_cover_count += dfs(left_board -1)
			block_convert(y, x, block, '.')
	return board_cover_count

T = int(input())
for _ in range(T):
	H, W = list(map(int, input().split()))
	board = [list(input()) for y in range(H)]

	if open_board_counter() % 3 == 0:
		print(dfs(int(open_board_counter() / 3)))
	else:
		print(0)
