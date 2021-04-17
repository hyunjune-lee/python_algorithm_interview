# 0. 날짜 & 시도 횟수
# 2021.01.28(목요일)
# 시도 횟수 : 1 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
#

from typing import *
from collections import *
import heapq

class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		move = [(-1,0),
				(1,0),
				(0,1),
				(0,-1)]

		count = 0
		m = len(grid)
		n = len(grid[0])
		for y in range(m):
			for x in range(n):
				if grid[y][x] == "1":
					stack = [(y,x)]
					count += 1
					while stack:
						ny, nx = stack.pop()
						if grid[ny][nx] == "1":
							grid[ny][nx] = "0"
							for my, mx in move:
								dy = ny + my
								dx = nx + mx
								if m > dy >= 0 and n > dx >=0:
									if grid[dy][dx] == "1":
										stack.append((dy,dx))
		return count








sol = Solution()
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(sol.numIslands(grid)) # 1
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol.numIslands(grid)) # 3

grid = [["1","0","1"],["0","1","0"],["1","0","1"]]
print(sol.numIslands(grid)) # 5

grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
print(sol.numIslands(grid)) # 1
