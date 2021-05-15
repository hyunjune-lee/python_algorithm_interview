num_str = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}


def solution(s):
    for num in range(10):
        s = s.replace(num_str[num], str(num))
    return s


print(solution("one zero4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))
