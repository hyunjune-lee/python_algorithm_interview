# 24분 걸림
# 거리를 측정할 때, 절댓값 안 해준것 그리고 x축 길이는 빼고 계산한 실수를 했다.


def solution(numbers, hand):
    def get_dist(a, b):
        ay, ax = a
        by, bx = b
        return abs(ay - by) + abs(ax - bx)

    answer = ""
    l_pos = (3, 0)
    r_pos = (3, 2)
    dic = dict()
    for i, l in enumerate([1, 4, 7]):
        dic[l] = (i, 0)
    for i, r in enumerate([3, 6, 9]):
        dic[r] = (i, 2)
    for i, m in enumerate([2, 5, 8, 0]):
        dic[m] = (i, 1)
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            l_pos = dic[num]
        elif num in [3, 6, 9]:
            answer += "R"
            r_pos = dic[num]
        else:
            if get_dist(dic[num], l_pos) == get_dist(dic[num], r_pos):
                if hand == "right":
                    answer += "R"
                    r_pos = dic[num]
                else:
                    answer += "L"
                    l_pos = dic[num]
            elif get_dist(dic[num], l_pos) < get_dist(dic[num], r_pos):
                answer += "L"
                l_pos = dic[num]
            else:
                answer += "R"
                r_pos = dic[num]

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
