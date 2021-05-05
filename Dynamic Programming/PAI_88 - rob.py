from typing import List

# a[i] = max(a[i-2] + num[i], a[i-1])
class Solution:
    def rob(self, nums: List[int]) -> int:
        a = [0 for _ in range(len(nums) + 2)]
        for i in range(2, len(nums) + 2):
            a[i] = max(a[i - 2] + nums[i - 2], a[i - 1])
            print(a)
        return a[-1]


sol = Solution()
print(sol.rob([1, 2, 3, 1]))  # 4
print(sol.rob([2, 7, 9, 3, 1]))  # 12
print(sol.rob([2, 1, 1, 2]))  # 4
# print(sol.climbStairs())
