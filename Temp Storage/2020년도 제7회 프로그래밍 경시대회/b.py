def is_all_same(c1, c2, c3):
    if c1 == c2 and c2 == c3 and c1 == c3:
        return True
    return False


def is_all_diff(c1, c2, c3):
    if c1 != c2 and c2 != c3 and c1 != c3:
        return True
    return False
    


def is_hap(first, second, third, visited):
    visit_check_list = sorted([first, second, third])
    if visit_check_list in visited:
        return False
    visited.append(visit_check_list)
    is_ok = False
    for i in range(3):
        if is_all_same(first, second, third) or is_all_diff(first, second, third):
            is_ok = False
        if not is_ok:
            return False
    return True
            
        


for _ in range(int(input())):
    a_score, b_score = 0, 0
    cards= []
    for _ in range(9):
        shape, color, back= input().split()
        cards.append((shape, color, back))

    input_str = input()
    i = 1
    visited = []
    while input_str[0] != "G":
        first, second, third = input_str[1:].split()
        if is_hap(cards[first], cards[second], cards[third], visited):
            if i % 2 == 1: # 홀수이면 A
                a_score += 1
            else:
                b_score += 1
        else:
            if i % 2 == 1: # 홀수이면 A
                a_score -= 1
            else:
                b_score -= 1           

        input_str = input()


