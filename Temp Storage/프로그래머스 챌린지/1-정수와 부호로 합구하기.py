def solution(absolutes, signs):
    answer = 0
    for i, num in enumerate(absolutes):
        answer += num if signs[i] else -num
    return answer
