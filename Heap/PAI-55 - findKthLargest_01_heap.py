from typing import List
import heapq

# 2번째로 큰건 3번째로 작은거
# 4 - 2 + 1
# len(num) - k  + 1
# 1 2 3 4
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return heapq.heappop(nums)
