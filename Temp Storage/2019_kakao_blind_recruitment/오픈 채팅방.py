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
