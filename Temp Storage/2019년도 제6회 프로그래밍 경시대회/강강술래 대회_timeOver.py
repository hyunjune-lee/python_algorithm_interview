import math
from collections import defaultdict

prime_dict = dict()
def is_prime(num):
    if num in prime_dict :
        return prime_dict[num]
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            prime_dict[num] = False
            return False
    prime_dict[num] = True
    return True


def get_div(num):
    if num in div_dict:
        return div_dict[num]
    if is_prime(num):
        div_dict[num] = set([num])
        return 

    div_set = set()
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            div1 = num // i
            div2 = i
            if is_prime(div1):
                div_set.add(div1)
            else:
                div_set |= get_div(div1)
            if is_prime(div2):
                div_set.add(div2)
            else:
                div_set |= get_div(div2)
    div_dict[num] = div_set
    return div_set


def find(a):
    if parent_dict[a] == a:
        return a
    else:
        parent_dict[a] = find(parent_dict[a])
        return parent_dict[a]

def union(a, b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent != b_parent:
        parent_dict[b_parent] = a_parent
        div_dict[a_parent] |= div_dict[b_parent]
        child_dict[a_parent] += child_dict[b_parent]
        child_dict[b_parent] = 0


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    nums = nums[1:]
    parent_dict = dict() # 전부 자기 자신으로 셋팅
    # 공약수 set 각자거로 셋팅하고 후에 합쳐지면 부모한테 add하기
    div_dict = dict()
    # 초기화
    child_dict = defaultdict(int)
    for num in nums:
        parent_dict[num] = num
        get_div(num)
        child_dict[num] = 1
    # print(div_dict, prime_dict)

    # 방문한 최종 부모들, 아직 방문하지 않은 녀석들
    visited_dict = dict()
    for num in nums:
        is_union = False
        for parent, divs in visited_dict.items():
            # 겹치는게 하나라도 있다면 union
            # 멈추는게 아니라 계속 union 해야겠는데.. 어떻게하지
            if len(div_dict[num] & divs) >= 1:
                is_union = True
                union(parent, num)
                visited_dict[parent] = div_dict[parent]
                # break
        if not is_union:
            visited_dict[num] = div_dict[num]


    # print(visited_dict)
    # print("parent_dict", parent_dict)
    # print("child_dict", child_dict)
    res = 0
    for child_cnt in child_dict.values():
        if res < child_cnt:
            res = child_cnt
    print(res)
