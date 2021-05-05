from typing import List

# A[i] = max(A[i-1] + e[i], e[i])
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            a[i] = max(a[i - 1] + nums[i], nums[i])

        return max(a)


sol = Solution()
print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(sol.maxSubArray([1]))
print(sol.maxSubArray([5, 4, -1, 7, 8]))
