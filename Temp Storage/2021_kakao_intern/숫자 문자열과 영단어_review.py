# [0. 날짜]
# 2021.08.22(일요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 글자가 나오면 앞에 2글자를 가지고 판단하고 판단된 숫자만큼 인덱스 진행하기
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
num_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def solution(s):
    i = 0
    res = []
    while i < len(s):
        if "0" <= s[i] <= "9":
            res.append(s[i])
            i += 1
        else:
            for num_str, num in num_dict.items():
                if num_str[:2] == s[i : i + 2]:
                    res.append(str(num))
                    i += len(num_str)
    return int("".join(res))


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
