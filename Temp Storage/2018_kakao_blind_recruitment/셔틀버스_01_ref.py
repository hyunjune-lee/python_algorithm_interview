from collections import deque

# 일단은 시간을 전부 분으로 바꿔서 계산 8:00 => 60* 8 = 480
def solution(n, t, m, timetable):
    def convert_to_time(total_min):
        h, m = divmod(total_min, 60)
        return str(h).zfill(2) + ":" + str(m).zfill(2)

    time_q = [int(time[:2]) * 60 + int(time[3:]) for time in timetable]
    time_q.sort()
    time_q = deque(time_q)
    bus_time = 9 * 60
    for _ in range(n):
        for _ in range(m):
            # 대기가 있을때 1분 전 도착
            if time_q and time_q[0] <= bus_time:
                candidate = time_q.popleft() - 1
            else:  # 대기가 없는 경우 셔틀버스 시간 맞춰서 도착
                candidate = bus_time
        bus_time += t

    return convert_to_time(candidate)


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
print(solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]))
print(solution(1, 1, 1, ["23:59"]))
print(
    solution(
        10,
        60,
        45,
        [
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
        ],
    )
)

print(
    solution(
        10,
        60,
        10,
        [
            "17:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
            "23:59",
        ],
    )
)
