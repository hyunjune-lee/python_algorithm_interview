# [0. 날짜]
# 2021.06.26(토요일)
# 문제 유형:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# Q. 유일성과 최소성을 어떻게 판별할 것인가?
# A. 최소성은.. 일단 부분집합에 포함되지 않음을 뜻한다.
# 예를 들어 학번 자체가 후보키가 되면, 학번을 포함하는 후보키는 없다는 뜻이다.
# 유일성 판별은 해당하는 후보를 묶어서 tuple로 만들고 유일한지 체크하면 된다..
# 근데.. [이름 전공], [이름 학년] 이렇게 묶이는 경우..
# 1개일 때// 2개일 때 (1개인 후보키 포함 X) // 3개일때는 1개, 2개의 후보키를 포함하지 않게..? // 4개일때 1개
# 조합..
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
#
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기]
# 컬럼이 4개로 고정인 줄 알아서 for문 범위를 4로 고정했는데 보니깐 1~8개의 범위를 가지고 있어서 런타임 에러 및 실패뜸


from itertools import combinations


def solution(relation):
    candidate_keys = []
    relation_row_len = len(relation[0])
    for key_size in range(1, relation_row_len):
        for check_key_list in combinations(range(relation_row_len), key_size):
            check_relation_list = []
            for i in range(len(relation)):
                check_relation_list.append(tuple(relation[i][check_key] for check_key in check_key_list))
            # 유일성 체크
            if len(check_relation_list) == len(set(check_relation_list)):
                # 최소성 체크
                is_minimal = True
                for candidate_key in candidate_keys:
                    if len(set(candidate_key) & set(check_key_list)) == len(candidate_key):
                        is_minimal = False
                        break
                if is_minimal:
                    candidate_keys.append(check_key_list)

    # 각 튜플은 유일함으로 후보키는 최소 1개는 존재한다.
    return max(len(candidate_keys), 1)


print(set([0, 1]) & set([0, 1, 2]))
print(
    solution(
        [
            ["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"],
        ]
    )
)
