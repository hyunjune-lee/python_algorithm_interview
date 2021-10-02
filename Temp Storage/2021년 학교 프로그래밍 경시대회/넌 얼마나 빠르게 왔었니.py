from collections import defaultdict
import sys
input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))

dic = defaultdict(list)

for i in range(len(students)):
    dic[students[i]].append(i + 1)

for key, val in dic.items():
    dic[key] = " ".join(map(str ,val))

Q = int(input())
qs = list(map(int, input().split()))
for i in range(len(qs)):
    if dic[qs[i]]:
        print(dic[qs[i]])
    else:
        print(-1)


