# [0. 날짜]
# 2021.07.23(금요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# load  BOJBOJBOJ
# dp_en 012345678
# 처음부터 끝까지 진행하면서 B 이면 그 뒤에 나오는 모든 O에 대해서 점프값을 구하고
# O면 J, J이면 B 이런 식으로 해준다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution():
    for i in range(N):
        if dp_energy[i] != float("inf"):
            next_c = "O"
            if load[i] == "O":
                next_c = "J"
            elif load[i] == "J":
                next_c = "B"
            for j in range(i + 1, N):
                if load[j] == next_c:
                    jump_energy = dp_energy[i] +  (j - i) ** 2
                    if dp_energy[j] > jump_energy:
                        dp_energy[j] = jump_energy
    return dp_energy[N - 1] if dp_energy[N - 1] != float('inf') else -1


N = int(input())
load = input()
dp_energy = [float("inf") for _ in range(N)]
dp_energy[0] = 0
print(solution())
