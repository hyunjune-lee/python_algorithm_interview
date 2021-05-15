from collections import deque


def solution(n, k, cmd):
    table = ["O"] * n
    select = k
    del_stack = []
    for command in cmd:
        if command[0] == "U":
            select -= int(command[2:])
        elif command[0] == "D":
            select += int(command[2:])
        elif command[0] == "C":
            table.pop(select)
            del_stack.append(select)
            # print("del ", select)
            if select == len(table):
                select -= 1
        elif command[0] == "Z":
            c = del_stack.pop()
            # print(c)
            if c <= select:
                select += 1
            table.insert(c, "O")

        # print(select, table)
    while del_stack:
        c = del_stack.pop()
        # print(c)
        table.insert(c, "X")
        # print(table)

    return "".join(map(str, table))


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
