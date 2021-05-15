# 한 대기실의 5x5를 돌면서
# P가 나올때마다 주변을 체크?
# 대각선일때는 둘다,
# 직선일때는 사이만
# 바로 주변일때는 바로 아웃

# 직선일 때 이거 2곱해서 p체크하고 이걸로 파티션 체크
no_dist = [[-1, 0], [0, 1], [1, 0], [0, -1]]
# 대각선할때 no_dist 2개씩 체크 0 일때 0,1// 1일때 1,2 이런식으로 3일때 3, 0
check_cross_dist = [[-1, 1], [1, 1], [1, -1], [-1, -1]]


def boundary_check(y, x):
    if 0 <= y < 5 and 0 <= x < 5:
        return True
    return False


def place_check(place):
    for y in range(5):
        for x in range(5):
            if place[y][x] == "P":
                for dy, dx in no_dist:
                    # 바로 옆 체크
                    my = y + dy
                    mx = x + dx
                    if boundary_check(my, mx) and place[my][mx] == "P":
                        return 0
                    # 2칸 직선으로 떨어질때 체크
                    ny = y + 2 * dy
                    nx = x + 2 * dx
                    if boundary_check(ny, nx) and place[ny][nx] == "P" and place[my][mx] != "X":
                        return 0
                for idx, coord in enumerate(check_cross_dist):
                    dy, dx = coord
                    my = y + dy
                    mx = x + dx
                    if boundary_check(my, mx) and place[my][mx] == "P":
                        ny = y + no_dist[idx][0]
                        nx = x + no_dist[idx][1]
                        if place[ny][nx] != "X":
                            return 0
                        ny = y + no_dist[(idx + 1) % 4][0]
                        nx = x + no_dist[(idx + 1) % 4][1]
                        if place[ny][nx] != "X":
                            return 0
    return 1


def solution(places):
    res = []
    for place in places:
        res.append(place_check(place))

    return res


print(
    solution(
        [
            # ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            # ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
            # ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)
