# [0. 날짜]
# 2021.07.14(수요일)
# 문제 유형:문자열, 브루트포스 알고리즘, 비트마스킹, 백트래킹
# 걸린 시간: 1시간
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 남극문자를 읽기 위해 a n t i c 이 5글자는 필수이다. 이보다 아래면 읽을 수 없다.
# 각줄마다 접두사, 접미사를 뺀 가운데 단어의 글자를 set으로 변환하고, 이 set의 요소를 공통 set에 더해준다.
# 공통 set에서 조합으로 k - 5 만큼의 글자 set을 만들고 이거에 대해 각 줄의 단어 set이 포함되는지 체크한다.
# 최댓값을 반환해준다.
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# combinations를 쓸 때 고르는 개수를 K -5 로 했는데 이때 K-5가 total_set의 길이보다 길어지면 안된다.
# 그래서 고르는 개수 최대가 total_set 길이만큼이 되도록 한다.
# [Important] combinations 쓸 때 고르는 개수 범위 조심하자
from itertools import combinations


def solution(N, K, words):
    if K < 5:
        return 0
    elif K >= 26:
        return N
    total_set = set()
    word_set_list = list()
    for word in words:
        word_set = set(word) - {"a", "n", "t", "i", "c"}
        word_set_list.append(word_set)
        total_set |= word_set
    res = 0
    total_set -= {"a", "n", "t", "i", "c"}
    select_limit = K - 5 if K - 5 < len(total_set) else len(total_set)
    for teach_word in combinations(total_set, select_limit):
        teach_word_set = set(teach_word)
        learn_count = 0
        for word_set in word_set_list:
            if word_set.issubset(teach_word_set):
                learn_count += 1
        res = max(res, learn_count)
    return res


N, K = map(int, input().split())
words = []
for _ in range(N):
    words.append(input()[4:-4])
print(solution(N, K, words))
