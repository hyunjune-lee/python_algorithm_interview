# [0. 날짜]
# 2021.07.23(금요일)
# 문제 유형:
# 걸린 시간: 30분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# y는 n - 1, 가로는 20 이 배열을 만든다. 이때 각 배열에 존재하는 숫자는 가능한 등식의 개수이다.
# 순회하면서 등식의 개수가 존재하면 해당 인덱스에 다음줄의 숫자를  + - 를 해준 값을
# 다음줄에 현재의 등식의 개수만큼 더해준다.
# y는 n - 2까지 진행하고 board[마지막 줄 - 1][마지막 숫자]를 리턴해준다.
#     0  1  2  3 .5. 8 ... 20
# 8|0                1
# 3|1             1
# ....
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution():
    dp_board[0][nums[0]] = 1
    for y in range(0, N - 2):
        for num in range(21):
            if dp_board[y][num]:
                next_num = nums[y + 1]
                if num + next_num <= 20:
                    dp_board[y + 1][num + next_num] += dp_board[y][num]
                if num - next_num >= 0:
                    dp_board[y + 1][num - next_num] += dp_board[y][num]
    return dp_board[N - 2][nums[-1]]


N = int(input())
nums = list(map(int, input().split()))
dp_board = [[0 for _ in range(21)] for _ in range(N - 1)]


print(solution())
