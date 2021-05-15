# 비트연산 xor


def solution(numbers):
    res_list = []
    for num in numbers:
        if num % 4 == 3:
            bin_num = bin(num)
            i = len(bin_num) - 2
            next_num = "1"
            while i - 1 >= 0 and bin_num[i - 1] == "1":
                next_num += "1"
                i -= 1
            next_num = int("10" + next_num, 2)
            res_list.append(next_num)
        else:
            check_num = num + 1
            while bin(num ^ check_num).count("1") > 2:
                check_num += 1
            res_list.append(check_num)

    return res_list


print(solution([0, 2, 3, 7, 15]))
