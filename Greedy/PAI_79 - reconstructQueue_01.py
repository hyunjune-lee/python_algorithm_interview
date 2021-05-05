from typing import List
import heapq


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for p in people:
            heapq.heappush(heap, (-p[0], p[1]))
        res = []
        while heap:
            h, k = heapq.heappop(heap)
            h = -h
            k_count = k
            for i in range(len(res)):
                if k_count == 0:
                    k_count = -1
                    res.insert(i, (h, k))
                    break
                if h <= res[i][0]:
                    k_count -= 1
            if k_count != -1:
                res.append((h, k))
        return res


sol = Solution()
print(sol.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
