from collections import deque


def solution(cacheSize, cities):
    run_time = 0
    q = deque(maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city in q:
            run_time += 1
            q.remove(city)
            q.append(city)
        else:
            run_time += 5
            q.append(city)

    return run_time


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(
    solution(
        2,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ],
    )
)
print(
    solution(
        5,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ],
    )
)
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
