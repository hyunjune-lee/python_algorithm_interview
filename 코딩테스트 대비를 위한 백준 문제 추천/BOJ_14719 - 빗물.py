# [0. 날짜]
# 2021.07.14(수요일)
# 문제 유형: 구현, 시뮬레이션
# 걸린 시간: 15분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 각 칸의 좌우의 최대 높이를 각각 미리 구한다
# 두번째칸부터 시작해서 끝에서 두번째까지 가면서
# 해당 칸의 좌우의 최대 높이중에서 작은 값과 현재 칸의 차이만큼 물을 채운다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution(W, heights):
    left_max_heights = [0 for _ in range(W)]
    right_max_heights = [0 for _ in range(W)]
    left_max_height = heights[0]
    right_max_height = heights[-1]
    for i in range(1, W - 1):
        left_max_heights[i] = left_max_height
        left_max_height = max(left_max_height, heights[i])
        reverse_i = W - 1 - i
        right_max_heights[reverse_i] = right_max_height
        right_max_height = max(right_max_height, heights[reverse_i])
    res = 0
    for i in range(1, W - 1):
        gap = min(left_max_heights[i], right_max_heights[i]) - heights[i]
        res += gap if gap > 0 else 0
    return res


H, W = map(int, input().split())
heights = list(map(int, input().split()))
print(solution(W, heights))
