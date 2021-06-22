from itertools import permutations
import math

# [원에 대한 아이디어]
# n을 더한 만큼의 리스트를 만들어준다. 그리고 weak 사이즈만큼만 검색하면 된다.


def solution(n, weak, dist):
    if max(dist) >= n:
        return 1
    min_cnt = math.inf
    weak_size = len(weak)
    weak += [w + n for w in weak]
    for start_idx in range(weak_size):
        for dist_list in permutations(dist, len(dist)):
            cnt = 1
            pos = start_idx
            for i in range(1, weak_size):
                next_pos = start_idx + i
                diff = weak[next_pos] - weak[pos]
                # 현재 dist 로 커버할 수 없을 때
                if diff > dist_list[cnt - 1]:
                    cnt += 1
                    pos = next_pos
                    if cnt > len(dist):
                        break

            if cnt <= len(dist):
                min_cnt = min(min_cnt, cnt)

    return min_cnt if min_cnt != math.inf else -1


print(
    solution(
        12,
        [1, 5, 6, 10],
        [1, 2, 3, 4],
    )
)
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
