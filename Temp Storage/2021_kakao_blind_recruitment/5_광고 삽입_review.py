# [0. 날짜]
# 2021.08.29(일요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 슬라이딩 윈도우? 각 분기점마다?
# 1. 재생시간을 초로 바꾼다.
# 2. 각 logs의 구간별로 시작과 끝을 분기점으로 삼아서
# 각 분기점 사이의 중복되는 구간의 개수를 구한다.
# 3. 각 분기점을 기준으로 전체? 슬라이딩 윈도우를 통해 누적 재생시간을 구해본다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# point_list 를 for 문안에서 선언을 해줘서 값이 모이지가 않았다..
# 중간마다 값 체크 해주기
from collections import deque


def time_to_sec(time):
    h, m, s = time.split(":")
    sec = int(s)
    sec += int(h) * 60 * 60
    sec += int(m) * 60
    return sec


def sec_to_time(sec):
    h = sec // (60 * 60)
    m = (sec % (60 * 60)) // 60
    s = sec % 60
    res = ""
    if h < 10:
        res += "0"
    res += str(h) + ":"
    if m < 10:
        res += "0"
    res += str(m) + ":"
    if s < 10:
        res += "0"
    res += str(s)

    return res


def solution(play_time, adv_time, logs):
    cum_play_time = [0 for _ in range(time_to_sec(play_time) + 1)]
    point_list = []
    for log in logs:
        start_time, end_time = log.split("-")
        point_list.append((time_to_sec(start_time), +1))
        point_list.append((time_to_sec(end_time), -1))
    before_point, cur_change = 0, 0
    for point, change in sorted(point_list):
        # print(sec_to_time(before_point), sec_to_time(point), change)
        for sec in range(before_point, point):
            cum_play_time[sec] = cur_change
        before_point = point
        cur_change += change

    max_adv_sum = 0
    cur_adv_sum = 0
    max_adv_sec = 0
    adv_time_sec = time_to_sec(adv_time)
    for adv_sec in range(adv_time_sec):
        cur_adv_sum += cum_play_time[adv_sec]
    max_adv_sum = cur_adv_sum
    for cur_sec in range(adv_time_sec, time_to_sec(play_time)):
        cur_adv_sum += cum_play_time[cur_sec] - cum_play_time[cur_sec - adv_time_sec]
        if max_adv_sum < cur_adv_sum:
            max_adv_sum = cur_adv_sum
            max_adv_sec = cur_sec - adv_time_sec + 1

    return sec_to_time(max_adv_sec)


print(
    solution(
        "02:03:55",
        "00:14:15",
        ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"],
    )
)


print(
    solution(
        "99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
    )
)
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))
