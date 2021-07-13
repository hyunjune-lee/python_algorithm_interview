# [0. 날짜]
# 2021.07.13(화요일)
# 문제 유형:브루트포스 알고리즘
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 9C2
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 출력 후 returne을 안해줘서 여러 케이스가 있을 때 전부 출력되어서 틀림

from itertools import combinations


def find_seven_dwarf(dwarf_heights):
    sum_height = sum(dwarf_heights)
    for a, b in combinations(range(9), 2):
        if sum_height - dwarf_heights[a] - dwarf_heights[b] == 100:
            for i, dwarf_height in enumerate(dwarf_heights):
                if i != a and i != b:
                    print(dwarf_height)
            return


dwarf_heights = []
for _ in range(9):
    dwarf_heights.append(int(input()))
find_seven_dwarf(sorted(dwarf_heights))
