from collections import deque

# 일단은 시간을 전부 분으로 바꿔서 계산 8:00 => 60* 8 = 480
def solution(n, t, m, timetable):
    def convert_to_time(total_min):
        return str(total_min // 60).zfill(2) + ":" + str(total_min % 60).zfill(2)

    time_q = []
    for time in timetable:
        hour, min = time.split(":")
        total_min = int(hour) * 60 + int(min)
        time_q.append(total_min)
    time_q = sorted(time_q)
    time_q = deque(time_q)
    bus_time = 9 * 60
    bus_list = []
    for _ in range(n):
        count = m
        bus = []
        while count > 0 and time_q:
            if time_q[0] <= bus_time:
                bus.append(time_q.popleft())
                count -= 1
            else:
                break
        is_empty = count != 0
        bus_list.append((bus_time, is_empty, bus))
        bus_time += t

    last_bus_info = bus_list[-1]
    # 비어있으면 버스 셔틀시간에
    if len(last_bus_info[2]) < m:
        return convert_to_time(last_bus_info[0])
    # 안 비어있으면
    else:
        return convert_to_time(max(last_bus_info[2]) - 1)


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
