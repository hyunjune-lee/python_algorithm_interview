n = int(input())

for _ in range(n):
    boggle = []
    for i in range(5):
        boggle.append(input())
    word_count = int(input())
    for j in range(word_count):
        find_word(input())


def find_word(word):
    for y in range(5):
        for x in range(5):
            boggle[y][x] = word[0]
