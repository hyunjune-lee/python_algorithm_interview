
from collections import defaultdict

for _ in range(int(input())):
    block_cnt = int(input())
    blocks = list(map(int, input().split()))
    set_limit = int(input())
    block_dict = defaultdict(int)
    l, r = 0, 0
    res = 0

    def dfs(l, r):
        global res
        if r == len(blocks) and len(block_dict) < set_limit:
            return
        elif r < len(blocks) and  len(block_dict) < set_limit:
            block_dict[blocks[r]] += 1
            dfs(l, r + 1)
            block_dict[blocks[r]] -= 1
        elif r < len(blocks) and len(block_dict) == set_limit:
            res += 1
            print(block_dict)
            block_dict[blocks[r]] += 1
            dfs(l, r + 1)
            block_dict[blocks[r]] -= 1
            block_dict[blocks[l]] -= 1
            if block_dict[blocks[l]] == 0:
                del block_dict[blocks[l]]
            dfs(l + 1, r)
            block_dict[blocks[l]] += 1
            
        elif r == len(blocks) and len(block_dict) == set_limit:
            res += 1
            print(block_dict)
            block_dict[blocks[l]] -= 1
            if block_dict[blocks[l]] == 0:
                del block_dict[blocks[l]]
            dfs(l + 1, r)
            block_dict[blocks[l]] += 1
        elif  len(block_dict) > set_limit:
            block_dict[blocks[l]] -= 1
            if block_dict[blocks[l]] == 0:
                del block_dict[blocks[l]]
            dfs(l + 1, r)
            block_dict[blocks[l]] += 1
    dfs(0,0)


    print(res)
    # elif r == len(blocks) and l < len(blocks):
    #     block_dict[blocks[l]] -= 1
    #     if block_dict[blocks[l]] == 0:
    #         del block_dict[blocks[l]]
    #     l += 1





