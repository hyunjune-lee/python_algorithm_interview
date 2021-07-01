# [0. 날짜]
# 2021.07.01(목요일)
# 문제 유형:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 1. 여벌 체육복을 가져왔지만 체육복을 잊어버린 경우를 제외해서 진짜 reserve를 구한다.
# 2. lost인 학생을 발견했을 때 먼저 왼쪽 학생, 오른쪽 학생순으로 reserve인지 확인하는데
#    만약 reserve이면 제외시키고 해당 lost 학생도 제외한다.
#    체육복 가진 학생 수를 늘린다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]

# <잃어버린 친구 기준>
# def solution(n, lost, reserve):
#     res = [1 for _ in range(n + 1)]
#     res[0] = 0
#     for r in reserve:
#         res[r] = 2
#     for l in lost:
#         res[l] -= 1
#     for i in range(1, n + 1):
#         if res[i] < 1:
#             # 왼쪽 친구가 여벌 체육복이 있을때
#             if i - 1 >= 1 and res[i - 1] == 2:
#                 res[i - 1] -= 1
#                 res[i] += 1
#             # 아니면 오른쪽 친구가 여벌 체육복이 있을때
#             elif i + 1 <= n and res[i + 1] == 2:
#                 res[i + 1] -= 1
#                 res[i] += 1
#         print(res)

#     return sum([1 if r != 0 else 0 for r in res])
# ==================================

# <여벌 체육복을 가진 친구 기준>
def solution(n, lost, reserve):
    res = [1 for _ in range(n + 1)]
    res[0] = 0
    for r in reserve:
        res[r] = 2
    for l in lost:
        res[l] -= 1
    for i in range(1, n + 1):
        if res[i] == 2:
            # 왼쪽 친구가 체육복이 없을때
            if i - 1 >= 1 and res[i - 1] == 0:
                res[i - 1] = 1
                res[i] = 1
            # 오른쪽 친구가 체육복이 없을때
            elif i + 1 <= n and res[i + 1] == 0:
                res[i + 1] = 1
                res[i] = 1
            else:  # 양쪽 친구가 체육복이 있으면 여벌의 체육복은 의미 X
                res[i] = 1

    return sum(res)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
