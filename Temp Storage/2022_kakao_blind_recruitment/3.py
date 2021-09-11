# [0. 날짜]
# 2021.09.11(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
from collections import defaultdict
import math


def time_to_min(time):
    res = 0
    hour, min = time.split(":")
    res += int(hour) * 60
    res += int(min)
    return res


def min_to_pay(fees, stay_min):
    default_time, default_pay, unit_time, unit_pay = fees
    if stay_min <= default_time:
        return default_pay
    pay = default_pay
    over_time = stay_min - default_time
    pay += math.ceil(over_time / unit_time) * unit_pay
    return pay


def solution(fees, records):
    car_dict = defaultdict(list)  # 입차이면 입차된 시간, 없으면 빈 리스트
    car_stay_min_dict = defaultdict(int)
    car_pay_dict = defaultdict(int)
    for record in records:
        time, car, state = record.split()
        if car_dict[car]:  # 있으면 입차된 상태이므로 출차하자
            in_min = car_dict[car][0]
            out_min = time_to_min(time)
            car_stay_min_dict[car] += out_min - in_min
            car_dict[car].pop()
        else:  # 없으면 입차시키자
            car_dict[car].append(time_to_min(time))
    # 출차 안한 차량 조사하기
    for still_in_car in car_dict:
        if car_dict[still_in_car]:
            car_stay_min_dict[still_in_car] += 1439 - car_dict[still_in_car][0]
            car_dict[still_in_car].pop()

    # print(car_stay_min_dict)
    res = []
    for car in sorted(car_stay_min_dict):
        res.append(min_to_pay(fees, car_stay_min_dict[car]))
    # print(car_dict)
    # print(car_pay_dict)
    return res


print(
    solution(
        [180, 5000, 10, 600],
        [
            "05:34 5961 IN",
            "06:00 0000 IN",
            "06:34 0000 OUT",
            "07:59 5961 OUT",
            "07:59 0148 IN",
            "18:59 0000 IN",
            "19:09 0148 OUT",
            "22:59 5961 IN",
            "23:00 5961 OUT",
        ],
    )
)
print(
    solution([120, 0, 60, 591], ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"])
)
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
