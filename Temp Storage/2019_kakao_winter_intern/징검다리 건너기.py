# [0. 날짜]
# 2021.09.08(수요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 위에서부터 탐색할때간격이 k 칸보다 전부 작은 숫자 바로 위
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 이진탐색 응용.. 여기서 이렇게 쓰일줄이야..
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def solution(stones, k):
    l, r = 1, 200000001
    while l < r:
        cnt = 0
        mid = (l + r) // 2
        for i in range(len(stones)):
            if stones[i] - mid <= 0:
                cnt += 1
                if cnt >= k:
                    r = mid
                    break
            else:
                cnt = 0
        if cnt < k:
            l = mid + 1
    return l


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
