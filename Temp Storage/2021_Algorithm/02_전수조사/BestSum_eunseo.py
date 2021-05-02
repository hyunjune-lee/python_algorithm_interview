def solution(target, nums, path):
    if target < 0:
        return None
    if target == 0:
        return path
    best_path = []
    for num in nums:
        nlist = solution(target - num, nums, path + [num])
        if nlist:
            # print("best",best_path)
            if not best_path or len(nlist) < len(best_path): #best path에 들은게 없음
                best_path = nlist
                ret_list.append(best_path)
    return best_path


# 입력 및 실행
for _ in range(int(input())):
    M, N = map(int, (input().split()))
    nums = list(map(int, (input().split())))
    # if M == 0:
    #     print(0)
    #     continue
    ret_list = []
    result = solution(M, nums, [])
    print(ret_list)
    if not result:
        print("-1")
    else:
        answer = " ".join(map(str, result))
        print(len(result), answer)
