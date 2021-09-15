# [0. 날짜]
# 2021.09.14(화요일)
# 문제 유형:
# 걸린 시간:
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
#
# [2. 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지]
# 분류기호의 문자열과, float를 같이 넣어주고 정렬은 float로 값은 문자열로 해주었다.
# [3. +개선 사항]
#
# [4. +한번에 맞추지 못한 경우 오답 원인 적기] 
# float로 바꾸었는데.. 813도 813.0 이렇게나와서..
# 단순히 문자열로 하면 길이에 따라서 정렬이이상하게 될 수도..?
# 처음에 float로 바꾸었는데 813이 813.0으로 나와서 
# 다시 문자열로 바꾸었는데 이러면 813 다음에 9 가 나온다..
# 9는 813보다 미리 나와야하는데..
# 그래서 분류기호의 문자열과, float를 같이 넣어주고 정렬은 float로 값은 문자열로 해주었다.

def getBook(str):
    a,b = str.split()
    b1, b2, b3 = b[0], int(b[1:3]), b[3]
    return (a, float(a), b1, b2, b3)


for _ in range(int(input())):
    books = []
    for _ in range(int(input())):
        books.append(getBook(input()))
    for _ in range(int(input())):
        books.append(getBook(input()))

    books.sort(key= lambda x: (x[1], x[2], x[3], x[4]))
    for book in books:
        s = book[0]
        s += " " + book[2]
        if book[3] < 10:
            s += "0"
        s += str(book[3])
        s += book[4]
        print(s)

# for _ in range(int(input())):
#     books = []
#     for _ in range(int(input())):
#         books.append(input())
#     for _ in range(int(input())):
#         books.append(input())

#     books.sort()
#     for book in books:
#         print(book)
