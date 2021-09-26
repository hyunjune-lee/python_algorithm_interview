# [0. 날짜]
# 2021.09.09(목요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 일단 모든 격자에 상하좌우로 보내봐야한다.
# 1 - 2- 2- 1
# 1 d 2 l 2 u 1 r 1 d

# 2 - 2- 1- 1
# 1 u 2 r 2 d 1 l 1 u
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution(grid):
    cycle_list = set()

    def dfs(y, x, direction, visited):
        move_info = (y, x, direction)
        if move_info in visited:
            cycle_list.add(tuple(sorted(visited)))
            return
        visited.append(move_info)
        if direction == "u":
            my, mx = y - 1, x
        elif direction == "d":
            my, mx = y + 1, x
        elif direction == "l":
            my, mx = y, x - 1
        elif direction == "r":
            my, mx = y, x + 1
        if my == -1:
            my = len(grid) - 1
        elif my == len(grid):
            my = 0
        elif mx == -1:
            mx = len(grid[0]) - 1
        elif mx == len(grid[0]):
            mx = 0
        # print(y, x, my, mx, direction)
        if grid[my][mx] == "L":
            if direction == "u":
                direction = "l"
            elif direction == "d":
                direction = "r"
            elif direction == "l":
                direction = "d"
            elif direction == "r":
                direction = "u"
        elif grid[my][mx] == "R":
            if direction == "u":
                direction = "r"
            elif direction == "d":
                direction = "l"
            elif direction == "l":
                direction = "u"
            elif direction == "r":
                direction = "d"
        dfs(my, mx, direction, visited)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for direction in ["u", "d", "l", "r"]:
                dfs(y, x, direction, [])

    return [len(cycle) for cycle in cycle_list]


print(solution(["SL", "LR"]))
print(solution(["S"]))
print(solution(["R", "R"]))
print(solution(["SRR", "SRR"]))
print(solution(["SRRLLL", "SRRLLLLRR"]))
print(solution(["SR", "SRRRRR"]))
