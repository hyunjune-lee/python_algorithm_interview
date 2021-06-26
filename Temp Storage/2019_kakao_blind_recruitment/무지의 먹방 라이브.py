# [0. 날짜]
# 2021.06.26(토요일)
# 문제 유형:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 1. 몇번째 아이템인지와 값을 같이 저장해둔다.
# 2. 먼저 k // food_times의 길이 => 5 // 3 => 1  (고정 -값)
# 5 % 3 = 2를 구한다.(k값)
# 3. food_times를 순회하면서 이 고정 - 값을 뺀다.
# 그결과 + 이면 next_foo_times에 넣고
# - 이면 k값에 더한다.
# 그리고 만약 고정 - 값이 없으면 next_food_times에서의 남은 k값에서의 index에 id가 정답이다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# k에 gap을 더해주는 것, 처음에 -1 처리
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
#


def solution(food_times, k):
    if k >= sum(food_times):
        return -1
    remain_foods = [(id + 1, food_time) for id, food_time in enumerate(food_times)]
    static_minus = k // len(remain_foods)
    k = k % len(remain_foods)
    while static_minus > 0:
        next_remain_foods = []
        for id, remain_food_time in remain_foods:
            gap = remain_food_time - static_minus
            if gap > 0:
                next_remain_foods.append((id, gap))
            elif gap < 0:
                k += -(gap)
        static_minus = k // len(next_remain_foods)
        k = k % len(next_remain_foods)
        remain_foods = next_remain_foods

    return remain_foods[k][0]


print(solution([3, 1, 2], 5))
print(solution([3, 3, 3], 9))
