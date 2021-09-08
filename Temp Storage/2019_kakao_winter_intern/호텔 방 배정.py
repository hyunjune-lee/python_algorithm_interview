# [0. 날짜]
# 2021.09.07(화요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 방문할때마다 해당 번호의 dict을 만들었다.
# dict은 처음에는 자기 번호 다음을 가리키도록 한다.
# 만약 배정되는 방에 이미 누가 배정되어있으면, 해당 노드가 가리키는 다음 노드로 이동한다.
# 이떄 이동하는 동시에 해당 노드에 다음 노드를 가리킬 리스트를 할당한다.
# 포인터 같은 개념이기 때문에 나중에 이 값을 바꿔서 탐색하는 모든 노드의 다음 지점을 한번에 바꾼다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
# 1등 코드 보니깐 리스트의 포인터 개념을 사용하지 않고 반복문 이후에
# 반복문을 한번 더 돌려서 이전의 노드가 모두 n + 1을 가리키도록 했다.
# 물론 포인터로 한번에 바꾸는 것보다는 느리다. 40~100ms 정도
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 커서 이진탐색으로 하려다가 링크드 리스트와 다이나믹을 이용한 것처럼
# 한번 지나간 곳은 제일 끝 지점으로 해놓는다.


def solution(k, room_number):
    visited_room = dict()
    res = []
    for room in room_number:
        next_room_pos = [room + 1]
        while room in visited_room:
            next_room = visited_room[room][0]
            visited_room[room] = next_room_pos
            room = next_room

        next_room_pos[0] = room
        visited_room[room] = [room + 1]
        res.append(room)

    return res


print(solution(10, [1, 3, 4, 1, 3, 1]))
