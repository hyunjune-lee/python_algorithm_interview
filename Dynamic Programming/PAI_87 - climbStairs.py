class Solution:
    def climbStairs(self, n: int) -> int:
        a = [0 for _ in range(n + 2)]
        a[0] = 1
        for cur_step in range(n):
            for add_step in (1, 2):
                a[cur_step + add_step] += a[cur_step]
        return a[n]


sol = Solution()
print(sol.climbStairs(2))
print(sol.climbStairs(3))
# print(sol.climbStairs())
