def solution(fruitWeights, k):
    dp = [0 for _ in range(len(fruitWeights) - k + 1)]
    dp[0] = max(fruitWeights[:k])
    max_count = 0
    for i in range(k):
        if dp[0] == fruitWeights[i]:
            max_count += 1

    for i in range(1, len(fruitWeights) - k + 1):
        if dp[i - 1] < fruitWeights[i + k - 1]:
            max_count = 1
            dp[i] = fruitWeights[i + k - 1]
        elif dp[i - 1] == fruitWeights[i + k - 1]:
            max_count += 1
            dp[i] = dp[i - 1]

            if fruitWeights[i - 1] == fruitWeights[i + k - 1]:
                max_count -= 1

        dp[i] = max(dp[i - 1], fruitWeights[i + k - 1])

    return sorted(dp, reverse=True)


print(solution([30, 40, 10, 20, 30], 3))
