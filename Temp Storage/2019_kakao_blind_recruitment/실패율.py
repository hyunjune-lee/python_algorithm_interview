# [0. 날짜]
# 2021.06.26(토요일)
# 문제 유형:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# 스테이지 1의 실패율 = 1의 개수 / stages의 전체 길이
# 스테이지 2의 실패율 = 2의 개수 / stages의 전체 길이에서 1의 개수를 뺀 숫자
# 스테이지 3의 실패율 = 3의 개수 / stages의 전체 길이에서 1의 개수와 2의 개수를 뺀 숫자
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 스테이지가 진행됨에 따른 실패율의 관계
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의하는 부분을 빠뜨림..
#         if stage_reach_player_count == 0:
#            fail_rate_list.append((0, stage_num))
from collections import Counter


def solution(N, stages):
    stage_count = Counter(stages)
    stage_reach_player_count = len(stages)
    fail_rate_list = []
    for stage_num in range(1, N + 1):
        if stage_reach_player_count == 0:
            fail_rate_list.append((0, stage_num))
        else:
            fail_rate_list.append((stage_count[stage_num] / stage_reach_player_count, stage_num))
        stage_reach_player_count -= stage_count[stage_num]
    fail_rate_list = sorted(fail_rate_list, key=lambda x: (-x[0], x[1]))
    return [fail_rate_list[i][1] for i in range(N)]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))
print(solution(4, [3, 3, 3, 3, 4]))
