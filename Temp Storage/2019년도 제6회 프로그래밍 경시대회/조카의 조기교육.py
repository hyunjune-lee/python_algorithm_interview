
from collections import defaultdict

for _ in range(int(input())):
    block_cnt = int(input())
    blocks = list(map(int, input().split()))
    set_limit = int(input())
    block_dict = defaultdict(int)
    l, r = 0, 0
    res = 0

    while True:
        if r == len(blocks) and len(block_dict) < set_limit:
            break
        elif r < len(blocks) and  len(block_dict) < set_limit:
            block_dict[blocks[r]] += 1
            r += 1
        elif r < len(blocks) and len(block_dict) == set_limit:
            res += 1
            # print(block_dict)
            block_copy_dict = block_dict.copy()
            copy_l = l
            while copy_l < r and copy_l < len(blocks) and len(block_copy_dict) == set_limit:
                block_copy_dict[blocks[copy_l]] -= 1
                if block_copy_dict[blocks[copy_l]] == 0:
                    del block_copy_dict[blocks[copy_l]]
                copy_l += 1
                if len(block_copy_dict) == set_limit:
                    res += 1
                    # print(block_copy_dict)

            block_dict[blocks[r]] += 1
            r += 1
        elif r == len(blocks) and len(block_dict) == set_limit:
            res += 1
            # print(block_dict)
            block_dict[blocks[l]] -= 1
            if block_dict[blocks[l]] == 0:
                del block_dict[blocks[l]]
            l += 1
        elif l < len(blocks) and len(block_dict) > set_limit:
            block_dict[blocks[l]] -= 1
            if block_dict[blocks[l]] == 0:
                del block_dict[blocks[l]]
            l += 1



    print(res)





