# [0. 날짜]
# 2021.08.24(화요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# + 자 모양으로 체크한다.
# 1. P(응시자)가 탐색되면 visite에 넣어두고 해당 기준으로 + 모양으로 P가있는지 탐색한다 있으면 0 반환
# 2. 그 다음에 + 모양으로 빈 테이블을 탐색한다.
# 만약 빈 테이블이 있으면 해당 테이블을 기준으로 + 모양으로 탐색하고
# 이때 visited되지 않은 P가 탐색되면 0을 반환한다.
# 1~2과정에서 0을 반환하지 않으면 1을 반환한다.
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def cross_check(place, y, x, c, visited):
    res = []
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        my = y + dy
        mx = x + dx
        if 0 <= my < 5 and 0 <= mx < 5:
            if place[my][mx] == c:
                if c == "P" and (my, mx) in visited:
                    continue
                res.append((my, mx))
    return res


def is_ok(place):
    visited = []
    for y in range(5):
        for x in range(5):
            if place[y][x] == "P":
                visited.append((y, x))
                if len(cross_check(place, y, x, "P", visited)) > 0:
                    return 0
                empty_tables = cross_check(place, y, x, "O", visited)
                if len(empty_tables) > 0:
                    for empty_table_y, empty_table_x in empty_tables:
                        if len(cross_check(place, empty_table_y, empty_table_x, "P", visited)) > 0:
                            return 0

    return 1


def solution(places):
    res = []
    for place in places:
        res.append(is_ok(place))
    return res


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)
