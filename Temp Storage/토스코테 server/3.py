def solution(amountText):
    # 가장 왼쪽 0, 구분자 체크
    if (len(amountText) >= 2 and amountText[0] == "0") or amountText[0] == ",":
        return False
    # 뒤에서부터 체크 구성요소 및 구분자 체크
    sep_check_i = 3
    sep_check = False
    amountReverseText = amountText[::-1]
    if len(amountReverseText) >= 5 and amountReverseText[3] == ",":
        sep_check = True
    for i, c in enumerate(amountReverseText):
        if sep_check and i == sep_check_i:
            if c == ",":
                sep_check_i += 4
                continue
            else:
                return False
        if c not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            return False
    return True


print(solution("10000"))
print(solution("25,000"))
print(solution("39,00"))
