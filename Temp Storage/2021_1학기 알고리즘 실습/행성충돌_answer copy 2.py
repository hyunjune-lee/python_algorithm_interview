# 양수 따로, 음수 따로 접근
# 양수 오른쪽 끝에서부터 오른쪽에 존재하는 자기보다 작은 애들 삭제한다.
# 그러다가 같은 크기를 만나면 둘다 없애고, 다음 오른쪽꺼부터 체크하기
def planet_crash(N, ps):
    stack = []
    for planet in ps:
        if planet > 0:
            stack.append(planet)
        else:
            if not stack or stack and stack[-1] < 0:
                stack.append(planet)
            else:
                while stack:
                    end_planet = stack[-1]
                    # 양수가 더 크면
                    if abs(planet) < end_planet:
                        break
                    elif abs(planet) == end_planet:  # 같으면
                        stack.pop()
                        break
                    elif abs(planet) > end_planet:  # 음수가 더 크면
                        stack.pop()
                        if not stack:
                            stack.append(planet)
                            break
    return stack


T = int(input())
for _ in range(T):
    N = int(input())
    ps = list(map(int, input().split()))
    print(" ".join(map(str, planet_crash(N, ps))))
