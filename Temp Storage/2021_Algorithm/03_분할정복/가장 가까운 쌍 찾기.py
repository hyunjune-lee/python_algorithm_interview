# 집합 P로부터 x 좌표를 기준으로 정렬된 Px와
# (델타 사이에 있는애들만?)y좌표를 기준으로 정렬된 Py를 확보 =>

# closestPair 알고리즘(Px, Py)
	# 단계 1. 다음 4개를 확보
		# Lx =  Px의 왼쪽 절반
		# Ly Px의 왼쪽 절반, y 좌표를 기준으로 정렬
		# Rx: Px의 오른쪽 절반
		# Ry Px의 오른쪽 절반, y 좌표를 기준으로 정렬
	# 단계 2. (base case <= 3: brute-force 방법)
		#l1,l2 = closestPair(Lx, Ly)
		#r1, r2 = closestPair(Rx, Ry)
		#s1, s2 = closestSplitPair(Px, Py) => O(n)
	# 단계 3. (l1, l2), (r1, r2), (s1, s2) 중 가장 가까운 쌍 반환
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

T = int(input())
for _ in range(T):
	N = int(input())
	elems = list(map(int, input().split()))
	coords = list(zip(elems[::2], elems[1::2]))
	px = sorted(coords, key = lambda x: x[0])
	py = sorted(coords, key = lambda x: x[1])
	ans = closest_pair(px, py)
	print(format(ans, ".2f"))
