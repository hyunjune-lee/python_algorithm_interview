import re


def score_cal(score, bonus):
    if bonus == "S":
        return score
    elif bonus == "D":
        return score ** 2
    elif bonus == "T":
        return score ** 3


def solution(dartResult):
    dart_list = re.findall(r"[0-9]+[SDT][*#]*", dartResult)
    score_list = [0] * len(dart_list)
    for i, dart in enumerate(dart_list):
        score, bonus, option = re.split(r"([SDT])", dart)
        score_list[i] = score_cal(int(score), bonus)
        if len(option) > 0:
            if option == "*":
                score_list[i] *= 2
                if i != 0:
                    score_list[i - 1] *= 2
            elif option == "#":
                score_list[i] *= -1

    return sum(score_list)


print(solution("1S2D*3T"))  # 37
print(solution("1D2S#10S"))  # 9
print(solution("1D2S0T"))  # 3
print(solution("1S*2T*3S"))  # 23
print(solution("1D#2S*3S"))  # 5
print(solution("1T2D3D#"))  # -4
print(solution("1D2S3T*"))  # 59
