# def count_pairings(taken):
#     first_free = -1
#     for i in range(n):
#         if not taken[i]:
#             first_free = i
#             break

#     if first_free == -1:
#         return 1
#     ret = 0
#     for pair_with in range(first_free + 1, n):
#         if not taken[pair_with] and areFriends[first_free][pair_with]:
#             taken[first_free] = taken[pair_with] = True
#             ret += count_pairings(taken)
#             taken[first_free] = taken[pair_with] = False
#     return ret


# C = int(input())

# for _ in range(C):
#     n, m = map(int, input().split())
#     areFriends = [[False for col in range(10)] for row in range(10)]
#     taken = [False for j in range(10)]
#     partner = list(map(int, input().split()))
#     for i in range(0, len(partner), 2):
#         areFriends[partner[i]][partner[i + 1]] = True
#         areFriends[partner[i + 1]][partner[i]] = True
#     print(count_pairings(taken))


N = int(input())

count = 0
router = []
while(True):
	info = int(input())
	if info == -1:
		break
	elif info == 0:
		router.pop(0)
		count -= 1
		continue
	elif count < N:
		count += 1
		router.append(info)

if len(router) == 0:
	print("empty")
else:
	for e in router:
		print(e, end = ' ')
