# 양수 따로, 음수 따로 접근
# 양수 오른쪽 끝에서부터 오른쪽에 존재하는 자기보다 작은 애들 삭제한다.
# 그러다가 같은 크기를 만나면 둘다 없애고, 다음 오른쪽꺼부터 체크하기
def planet_crash(N, ps):
    check_idx = N - 1
    while check_idx >= 0:
        if ps[check_idx] > 0:
            crash_check_idx = check_idx + 1
            while crash_check_idx < len(ps):
                if ps[crash_check_idx] > 0:
                    break
                elif ps[crash_check_idx] < 0:  # 음수이면
                    # 양수가 더 크면
                    if abs(ps[crash_check_idx]) < ps[check_idx]:
                        ps.pop(crash_check_idx)
                        check_idx = len(ps)
                        break
                    elif abs(ps[crash_check_idx]) == ps[check_idx]:  # 충돌시 같으면
                        ps.pop(crash_check_idx)
                        ps.pop(check_idx)
                        check_idx = len(ps)
                        break
                    elif abs(ps[crash_check_idx]) > ps[check_idx]:  # 양수가 더 작으면
                        ps.pop(check_idx)
                        check_idx = len(ps)
                        break

        check_idx -= 1
    return ps


T = int(input())
for _ in range(T):
    N = int(input())
    ps = list(map(int, input().split()))
    print(" ".join(map(str, planet_crash(N, ps))))
