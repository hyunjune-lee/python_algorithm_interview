from itertools import combinations

# 모든 노드의 left, right가 자를 여지가 있음
# right를 끊으면 right <-> val하고 left의 함
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.total_sum = 0
        self.left = left
        self.right = right


def post_order(node):
    if node is None:
        return 0
    sum = node.val
    sum += post_order(node.left)
    sum += post_order(node.right)
    node.total_sum = sum
    return sum


def solution(k, num, links):
    node_list = [None] * len(num)
    for i, n in enumerate(num):
        node_list[i] = TreeNode(n)
    root_check = [x for x in range(len(num))]
    parent_nodes = list()
    for i, link in enumerate(links):
        left, right = link
        if left != -1:
            node_list[i].left = node_list[left]
            root_check.remove(left)
            parent_nodes.append((i, "left"))
        if right != -1:
            node_list[i].right = node_list[right]
            root_check.remove(right)
            parent_nodes.append((i, "right"))
    # print(parent_nodes)
    root_node = node_list[root_check[0]]
    post_order(root_node)
    if k == 1:
        return root_node.total_sum
    root_node_total_sum = root_node.total_sum
    res = float("inf")
    for dis_cons in combinations(parent_nodes, k - 1):
        # print(dis_cons)
        total_sum = root_node_total_sum
        sum_group = []
        for node, child in dis_cons:
            node = node_list[node]
            if child == "right":
                total_sum -= node.right.total_sum
                node.total_sum -= node.right.total_sum
                sum_group.append(node.right.total_sum)
            else:
                total_sum -= node.left.total_sum
                node.total_sum -= node.left.total_sum
                sum_group.append(node.left.total_sum)
        sum_group.append(total_sum)
        # print(sum_group)
        res = min(res, max(sum_group))
        post_order(root_node)

    return res


print(
    solution(
        3,
        [12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1],
        [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]],
    )
)
print(solution(1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(1, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(2, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
print(solution(4, [6, 9, 7, 5], [[-1, -1], [-1, -1], [-1, 0], [2, 1]]))
