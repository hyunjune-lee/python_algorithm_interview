# 비트연산 xor


def solution(numbers):
    res_list = []
    for num in numbers:
        check_num = num + 1
        diff_count = bin(num ^ check_num).count("1")
        while diff_count > 2:
            check_num += 2 ** (diff_count - 2) - 1
            diff_count = bin(num ^ check_num).count("1")
        res_list.append(check_num)
    return res_list


print(solution([2, 7]))
