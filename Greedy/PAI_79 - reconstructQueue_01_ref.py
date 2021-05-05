from typing import List
import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))
        res = []
        while heap:
            mh, k = heapq.heappop(heap)
            res.insert(k, (-mh, k))
        return res


sol = Solution()
print(sol.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
