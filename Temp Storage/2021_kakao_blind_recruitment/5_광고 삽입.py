def time_to_sec(time):
    hour, min, sec = time.split(":")
    return int(hour) * 3600 + int(min) * 60 + int(sec)


def set_two_digit(time):
    if time < 10:
        return "0" + str(time)
    return str(time)


def sec_to_time(sec):
    hour = sec // 3600
    min = (sec % 3600) // 60
    sec = sec % 60
    return set_two_digit(hour) + ":" + set_two_digit(min) + ":" + set_two_digit(sec)


def solution(play_time, adv_time, logs):
    logs_start_sec = []
    logs_end_sec = []
    play_time_sec = time_to_sec(play_time)
    adv_time_sec = time_to_sec(adv_time)
    total_time = [0 for _ in range(play_time_sec + 1)]
    for log in logs:
        start_time, end_time = log.split("-")
        start_sec = time_to_sec(start_time)
        end_sec = time_to_sec(end_time)
        logs_start_sec.append(start_sec)
        logs_end_sec.append(end_sec)
        total_time[start_sec] += 1
        total_time[end_sec] -= 1

    # total_time[x] = 시각 x부터 x+1까지 1초 간의 구간을 포함하는 재생 구간의 개수
    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i - 1]

    # 누적 재생시간
    # 빼면 누적된 재생 시간이 되어서?
    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i - 1]

    best_adv_time_sec = max_time_sec = -1
    for i in range(adv_time_sec - 1, play_time_sec):
        if i >= adv_time_sec:
            if max_time_sec < total_time[i] - total_time[i - adv_time_sec]:
                max_time_sec = total_time[i] - total_time[i - adv_time_sec]
                best_adv_time_sec = i - adv_time_sec + 1
        else:  # 처음에 시작부분
            max_time_sec = max(max_time_sec, total_time[i])
            best_adv_time_sec = i - adv_time_sec + 1

    return sec_to_time(best_adv_time_sec)


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
