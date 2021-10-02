# [0. 날짜]
# 2021.10.02(토요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 그레이코드로 모든 숫자를 해야되나
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기] 
# 그냥 숫자 1개씩 바꾸는 줄 알았네.. 하긴 그러면 시작하자 끝낼수도 있었겠다

memo_list = dict()
for k_memo in range(1, 17):
    memo = []
    for i in range(2 ** k_memo):
        bin_num_str = bin(i)
        bin_num = int(bin_num_str[2])
        for xor_idx in range(3, len(bin_num_str)):
            if bin_num_str[xor_idx] != bin_num_str[xor_idx -1]:
                bin_num = bin_num * 10 + 1
            else:
                bin_num = bin_num * 10 + 0
        memo.append(int(str(bin_num), 2))
    memo_list[k_memo] = " ".join(map(str, memo)) 


T = int(input())
for _ in range(T):
    K = int(input())
    print(memo_list[K])
            
    
