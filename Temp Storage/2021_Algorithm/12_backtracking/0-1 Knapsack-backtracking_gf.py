# 0/1 Knapsack - 백트래킹 풀이 + 설명


def promising(items, W, currProfit, currWeight, index):
    global max_profit
    if currWeight >= W:  # 담을 수 없으면 유망 X
        return False
    else:  # 담을 수 있으면 최대한 많이 담은 뒤 bound를 계산
        nextIndex = index + 1
        bound = currProfit
        totalWeight = currWeight
    while nextIndex < n and totalWeight + items[nextIndex][1] <= W:  # 모든 물건을 다 담거나 가방 최대 용량을 넘으면 종료
        totalWeight += items[nextIndex][1]
        bound += items[nextIndex][2]
        nextIndex += 1
    if nextIndex < n:
        bound += (W - totalWeight) * items[nextIndex][0]
    return bound > max_profit  # bound가 max_profit보다 크면 유망함


def knapsack(items, W, currProfit, currWeight, index):
    global max_profit
    if currWeight <= W and currProfit > max_profit:  # 갱신부(담을 수 있고 & profit이 더 클 때)
        max_profit = currProfit

    if promising(items, W, currProfit, currWeight, index):  # 유망성 검사
        # (1) 현재 물건을 넣고 다시 탐색하기
        knapsack(items, W, currProfit + items[index + 1][2], currWeight + items[index + 1][1], index + 1)
        # (2) 현재 물건을 넣지 않고 탐색하기
        knapsack(items, W, currProfit, currWeight, index + 1)


# W = 가방의 용량
# items = 물건을 가성비(무게/가치)가 높은 순으로 정렬 => [가성비, 무게, 가치]
# n = 물건의 개수

for _ in range(int(input())):
    max_profit = 0
    W, n = map(int, input().split())
    arr = list(map(int, input().split()))
    v, w = [], []
    for i in range(0, n * 2, 2):
        v.append(arr[i])
        w.append(arr[i + 1])

    items = []
    for i in range(n):
        items.append([(v[i] / w[i]), w[i], v[i]])  # 가성비, 무게, 가치
    items.sort(reverse=True)
    knapsack(items, W, 0, 0, -1)
    print(max_profit)
