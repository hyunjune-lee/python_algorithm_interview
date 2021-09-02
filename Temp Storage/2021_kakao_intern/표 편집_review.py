# [0. 날짜]
# 2021.09.02(목요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 배열과 링크드리스트를 같이 쓰는 것
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 아래일때 next 이고 위일떄 prev인게 헷갈렸따.
# index 넣을 떄 nodeArr.index(curNode) 이런식으로 했는데(미친짓)
# 처음에 prev, next 생성할떄 같이 넣어주었다.
# 복구될때 순서대로 복구된다!!!
# (처음에 나는 복구한 노드 중심으로 가장 가까운 원래 노드를 찾아서 연결하려했음..ㄷ)


class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None


def solution(n, k, cmd):
    nodeArr = [Node() for _ in range(n)]
    for i in range(1, n):
        nodeArr[i - 1].next = nodeArr[i]
        nodeArr[i].prev = nodeArr[i - 1]

    curNode = nodeArr[k]
    del_stack = []
    for str in cmd:
        first_char = str[0]
        if first_char == "D":
            num = int(str[2:])
            for _ in range(num):
                curNode = curNode.next
        elif first_char == "U":
            num = int(str[2:])
            for _ in range(num):
                curNode = curNode.prev
        elif first_char == "C":
            curNode.removed = True
            upNode = curNode.prev
            downNode = curNode.next
            if upNode:
                upNode.next = downNode
            if downNode:
                downNode.prev = upNode
            del_stack.append(curNode)
            if downNode == None:
                curNode = upNode
            else:
                curNode = downNode

        elif first_char == "Z":
            recoveryNode = del_stack.pop()
            upNode = recoveryNode.prev
            downNode = recoveryNode.next
            if upNode:
                upNode.next = recoveryNode
            if downNode:
                downNode.prev = recoveryNode

            recoveryNode.removed = False

    res = ""
    for node in nodeArr:
        if node.removed:
            res += "X"
        else:
            res += "O"
    return res


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
