# [0. 날짜]
# 2021.09.11(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 가져올지 말지
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 가장 낮은 개수가 제일 많은 경우를 정확히 집어야함
# 나는 dfs에서 먼저쏘는 케이스를 앞에두면 자동으로 될줄 알았음

max_gap_score = -float("inf")
max_gap_res = [-1]


def solution(n, info):
    global max_gap_res
    max_gap_res = []
    max_gap_score = -float("inf")

    # 만약 i= 10, 즉 0점일때 남은 개수있으면 다 쓰기
    def dfs(i, score, enemy_score, history, remain_arrow):
        # print(i, score, enemy_score, history, remain_arrow)
        if i == 10:
            global max_gap_res
            global max_gap_score
            gap_score = score - enemy_score
            history.append(remain_arrow)

            if gap_score > 0 and gap_score >= max_gap_score:
                if gap_score > max_gap_score:
                    max_gap_score = gap_score
                    max_gap_res = []
                max_gap_res.append(history[:])
                # print(history, score, enemy_score, gap_score)
            return score

        for get_score in [1, 0]:
            if get_score:  # 만약 이번 점수를 가져온다면
                need_arrow = info[i] + 1
                next_remain_arrow = remain_arrow - need_arrow
                if next_remain_arrow >= 0:
                    dfs(i + 1, score + 10 - i, enemy_score, history + [need_arrow], next_remain_arrow)
            else:  # 이번 점수를 포기한다면, 어피치의 점수가 올라가겠지 만약 1개라도 했으면
                need_arrow = 0
                if info[i]:
                    dfs(i + 1, score, enemy_score + 10 - i, history + [need_arrow], remain_arrow)
                else:
                    dfs(i + 1, score, enemy_score, history + [need_arrow], remain_arrow)

    dfs(0, 0, 0, [], n)
    if max_gap_res:
        reverse_max_gap_res = []
        for li in max_gap_res:
            reverse_max_gap_res.append(li[::-1])
        return sorted(reverse_max_gap_res, reverse=True)[0][::-1]

    return [-1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
