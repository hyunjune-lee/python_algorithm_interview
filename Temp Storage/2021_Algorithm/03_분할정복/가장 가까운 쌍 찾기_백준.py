
import math

def	closest_pair(px, py):
	if len(px) <= 3:
		min_dist = 100000
		for p1 in range(0 , len(px) - 1):
			for p2 in range(p1 + 1, len(px)):
				a = px[p1][0] - px[p2][0]
				b = px[p1][1] - px[p2][1]
				min_dist =  min(min_dist, math.sqrt(a * a + b * b))
		return min_dist


	mid = len(px) // 2
	px_left = px[:mid]
	py_left = [p for p in py if p[0] < px[mid][0]]
	px_right = px[mid:]
	py_right = [p for p in py if p[0] >= px[mid][0]]


	delta = min(closest_pair(px_left, py_left),closest_pair(px_right, py_right) )
	return closest_split_pair(px, py, delta)

def closest_split_pair(px, py, delta):
	mid_x = px[len(px)//2][0]
	candidates = [p for p in py
					if mid_x - delta < p[0] and p[0] < mid_x + delta ]
	for p1 in range(0 , len(candidates) - 1):
		limit = 0
		for p2 in range(p1 + 1, len(candidates)):
			if limit < 7:
				a = candidates[p1][0] - candidates[p2][0]
				b = candidates[p1][1] - candidates[p2][1]
				delta =  min(delta, math.sqrt(a * a + b * b))
				limit += 1
	return delta


N = int(input())
coords = []
for _ in range(N):
	coords.append(list(map(int, input().split())))
px = sorted(coords, key = lambda x: x[0])
py = sorted(coords, key = lambda x: x[1])
ans = closest_pair(px, py)
print(int(ans * ans))
