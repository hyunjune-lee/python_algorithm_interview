# [0. 날짜]
# 2021.07.14(수요일)
# 문제 유형: 그리디 알고리즘
# 걸린 시간: 15분
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 1. 멀티탭이 비어있으면 찰때까지 꽂는다.
# 2. 플러그를 빼는 경우.. 뒤에 안 나오거나, 제일 늦게 나오는 플러그를 뽑고 지금 플러그를 꽂는다.
#  (이건 멀티탭의 요소들을 뒤에 계속 비교하면서 같은게 나오면 제거해준다. 그래서 끝에 도달하거나 1개가 남을때까지)
#   (끝에 도달하면 아무거나 제외해주면 된다.)
# 3. 뽑을때마다 횟수 +1 해주기
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]


def find_last_appear_item(multitap, items):
    for item in items:
        if item in multitap:
            multitap.remove(item)
        if len(multitap) == 1:
            break
    return multitap[0]


def solution(N, K, items):
    multitap = []
    unplug_count = 0
    for i, item in enumerate(items):
        if item not in multitap:
            if len(multitap) < N:
                multitap.append(item)
            else:
                remove_item = find_last_appear_item(multitap[:], items[i:])
                multitap.remove(remove_item)
                multitap.append(item)
                unplug_count += 1
    return unplug_count


N, K = map(int, input().split())
items = list(map(int, input().split()))
print(solution(N, K, items))
