# [0. 날짜]
# 2021.06.26(토요일)
# 문제 유형:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution(record):
    order_list = []
    nickname_dict = {}
    for r in record:
        if r[0] == "E" or r[0] == "C":
            order, id, nickname = r.split()
            nickname_dict[id] = nickname
        else:
            order, id = r.split()
        order_list.append((order, id))

    answer = []
    for order, id in order_list:
        if order == "Enter":
            answer.append(nickname_dict[id] + "님이 들어왔습니다.")
        elif order == "Leave":
            answer.append(nickname_dict[id] + "님이 나갔습니다.")
    return answer


print(
    solution(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    )
)
