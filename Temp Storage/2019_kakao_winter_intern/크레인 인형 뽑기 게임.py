# [0. 날짜]
# 2021.09.03(금요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 각 moves에서 받은 move 열의 위에서부터 행을 내려오면서 0이 아닌 숫자를 발견하면
# board에서 빼서 stack에 넣는데
# 이때 맨 위의 블록과 같은지 확인하고 같으면 터트리고 아니면 그대로 넣는다
# 터트린 개수 * 2를 반환해준다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution(board, moves):
    basket = []
    res = 0
    for move in moves:
        for row in range(len(board)):
            if board[row][move - 1]:
                doll = board[row][move - 1]
                board[row][move - 1] = 0
                if basket and basket[-1] == doll:
                    basket.pop()
                    res += 2
                else:
                    basket.append(doll)
                break
    return res


print(
    solution(
        [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]
    )
)
