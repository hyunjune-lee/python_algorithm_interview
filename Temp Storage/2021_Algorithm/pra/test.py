import timeit


def sum_func(sum, i):
    return sum + i


start_time = timeit.default_timer()  # 시작 시간 체크

sum = 0

for i in range(10000000):
    # sum_func(sum, i)
    sum += i

terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))
