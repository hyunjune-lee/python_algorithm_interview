from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                max_profit += prices[i + 1] - prices[i]
        return max_profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
