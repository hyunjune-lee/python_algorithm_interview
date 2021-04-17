def quad_switch_updown(quad_zip, idx):
    c = quad_zip[idx]
    if c == "w" or c == "b":
        return c
    idx += 1
    up_left = quad_switch_updown(quad_zip, idx)
    idx += len(up_left)
    up_right = quad_switch_updown(quad_zip, idx)
    idx += len(up_right)
    down_left = quad_switch_updown(quad_zip, idx)
    idx += len(down_left)
    down_right = quad_switch_updown(quad_zip, idx)
    idx += len(down_right)
    return "x" + down_left + down_right + up_left + up_right


for _ in range(int(input())):
    print(quad_switch_updown(list(input()), 0))
