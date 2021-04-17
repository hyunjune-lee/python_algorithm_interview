# 0. 날짜 & 시도 횟수
# 2021.02.01(월요일)
# 시도 횟수 : 2 번째
# 1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지
#
# 2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
#
# 3. (+한번에 맞추지 못한 경우 오답 원인 적기)
# dfs로 한번의 탐색에서 중복된 노드가 나올시 순환임을 체크했는데
# 시간초과가 나왔다. 하지만 이미 한번 탐색한 노드는 True를 반환하게 하도록
# 가지치기 함으로써 문제를 해결했다.

from typing import *
from collections import *
import heapq
import itertools
import copy


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(node):
            if node in traced:
                return False
            if node in visited:
                return True
            traced.add(node)
            for next in graph[node]:
                if not dfs(next):
                    return False
            traced.remove(node)
            visited.add(node)

            return True

        traced = set()
        visited = set()
        for start in list(graph):
            if not dfs(start):
                return False
        return True


sol = Solution()
print(sol.canFinish(2, [[1, 0]]))  # True
print(sol.canFinish(2, [[1, 0], [0, 1]]))  # False
print(sol.canFinish(4, [[0, 1], [1, 2], [0, 3], [3, 2]]))  # False
