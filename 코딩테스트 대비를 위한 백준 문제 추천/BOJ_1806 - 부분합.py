# [0. 날짜]
# 2021.07.15(목요일)
# 문제 유형: 투포인터
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 왼쪽 포인터, 오른쪽 포인터를 이용해서 구한다.
# 왼쪽 포인터와 오른쪽 포인터 사이를 sub_sum이라 한다.
# 1. sub_sum이 S보다 작으면 오른쪽 포인터를 확장하고
# 2. sub_sum이 S보다 크거나 같으면 왼쪽 포인터를 진행시킨다.
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력하면 된다.
# 라는 조건을 나중에 읽어서 고쳐주었다.


def solution(N, S, seq):
    left_idx, right_idx = 0, 1
    sub_sum = seq[0]
    min_len = N + 1
    while left_idx < right_idx and left_idx < N and right_idx < N:
        while sub_sum < S and right_idx < N:
            sub_sum += seq[right_idx]
            right_idx += 1
        while sub_sum >= S and left_idx < N:
            cur_len = right_idx - left_idx
            if cur_len < min_len:
                min_len = cur_len
            sub_sum -= seq[left_idx]
            left_idx += 1
    return min_len if min_len != N + 1 else 0


N, S = map(int, input().split())
seq = list(map(int, input().split()))
print(solution(N, S, seq))
