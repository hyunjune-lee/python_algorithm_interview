# [0. 날짜]
# 2021.09.14(화요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 2개의 기울기 같으면 삼각형 불가
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기] 
# 같은 점이 있는 경우를 생각 못했음

for _ in range(int(input())):
    ay, ax, by, bx, cy,cx = map(int, input().split())
    # 같은 점 있으면 아웃
    if ay == by and ax == bx:
        print("No")
        continue
    if ay == cy and ax == cx:
        print("No")
        continue
    if cy == by and cx == bx:
        print("No") 
        continue
        

    if (bx - ax) == 0:
        ab_slide = float('inf')
    else:
        ab_slide = (by - ay) / (bx - ax)
    if (cx - bx) == 0:
        bc_slide = float('inf')
    else:
        bc_slide = (cy - by) / (cx - bx)
    if (cx - ax) == 0:
        ac_slide = float('inf')
    else:
        ac_slide = (cy - ay) / (cx - ax)
    # print(ab_slide, bc_slide, ac_slide)
    if ab_slide == bc_slide == ac_slide:
        print("No")
    else:
        print("Yes")
