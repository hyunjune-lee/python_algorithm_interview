from collections import Counter, defaultdict, OrderedDict
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = [x[1] for x in Counter(tasks).most_common()]
        res = 0
        n_count = 0
        while any(tasks):
            res += n_count
            n_count = n + 1
            for i, task in enumerate(tasks):
                if task > 0:
                    tasks[i] -= 1
                    n_count -= 1
                    res += 1
                if n_count == 0:
                    break
            tasks.sort(reverse=True)
        return res


sol = Solution()
print(sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
print(sol.leastInterval(["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2))
