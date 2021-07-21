# [0. 날짜]
# 2021.07.21(수요일)
# 문제 유형: bfs
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# heapq 이용?
# 처음에는 무조건 클립보드에 저장하고 시작한다.
# 그 이후부터는
# 1. 클립보드에 저장하기, 이때 현재 이모티콘 수가 클립보드와 같으면 하지 않는다.
# 2. 클립보드만큼 더하기
# 3. -1 삭제이다. 목표보다 클시에 이것만 실행한다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 이 문제에서는 클립보드에 저장할때 제자리에 있게 된다. 그래서
# checked 사용이 번거로운데 클립보드의 개수도 정해서 checked에 기록해둔다.
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
from collections import deque


def bfs():
    q = deque([(1, 1, 1)])
    checked[1].append(1)
    while q:
        emo_count, clip_board, time = q.popleft()
        # print(emo_count, clip_board, time)
        if S == emo_count:
            return time
        else:
            # 1. 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
            if emo_count != clip_board and emo_count not in checked[emo_count]:
                checked[emo_count].append(clip_board)
                q.append((emo_count, emo_count, time + 1))
            # 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
            if emo_count + clip_board < MAX and clip_board not in checked[emo_count + clip_board]:
                checked[emo_count + clip_board].append(clip_board)
                q.append((emo_count + clip_board, clip_board, time + 1))
            # 3. 화면에 있는 이모티콘 중 하나를 삭제한다.
            if 1 <= emo_count - 1 and clip_board not in checked[emo_count - 1]:
                checked[emo_count - 1].append(clip_board)
                q.append((emo_count - 1, clip_board, time + 1))


MAX = 1001
checked = [[] for _ in range(MAX + 1)]
S = int(input())
print(bfs())
