from collections import OrderedDict


def LRU_cache(C, order):
    def put(key, value):
        if key in cache:
            cache.move_to_end(key)
        cache[key] = value
        if len(cache) > C:
            cache.popitem(last=False)

    def get(key):
        if key in cache:
            cache.move_to_end(key)
            return cache[key]
        else:
            return -1

    cache = OrderedDict()
    i = 0
    while i < len(order):
        if order[i] == 0:
            put(order[i + 1], order[i + 2])
            i += 3
        else:
            print(get(order[i + 1]), end=" ")
            i += 2


T = int(input())
for _ in range(T):
    C, N = map(int, input().split())
    orders = list(map(int, input().split()))
    LRU_cache(C, orders)
