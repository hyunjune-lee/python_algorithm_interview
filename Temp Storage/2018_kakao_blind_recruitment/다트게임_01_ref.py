import re


def solution(dartResult):
    bonus = {"S": 1, "D": 2, "T": 3}
    option = {"": 1, "*": 2, "#": -1}
    p = re.compile("(\d+)([SDT])([*#]?)")
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == "*" and i > 0:
            dart[i - 1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


print(solution("1S2D*3T"))  # 37
# print(solution("1D2S#10S"))  # 9
# print(solution("1D2S0T"))  # 3
# print(solution("1S*2T*3S"))  # 23
# print(solution("1D#2S*3S"))  # 5
# print(solution("1T2D3D#"))  # -4
# print(solution("1D2S3T*"))  # 59
