# [0] 날짜
# 2021.06.24(목요일)
# 문제 유형: 트라이
# [1. 문제의 간단한 해법과 함께 어떤 방식으로 접근했는지]
# 트라이로 insert와 startswith를 구현하는데 insert와 startswith를 좀 변형해준다.
# insert 할때는 노드를 지나칠때마다 해당 노드의 count dict에서 현재 insert하는 단어의 길이를 key로 하는 값을 1개 올려준다. (해당 글자로부터 파생되는 단어를 파악하기 위해서)
# startswith 할때는 ?가 나오면 현재 노드에서 현재 단어의 길이 만큼 파생되는 단어의 수를 반환해준다.
# 이를 words의 각 단어를 뒤집은 reverse_trie도 만들어준다. 그리고 ? 처음에 안 나오는 query는 이 reverse_trie를 통해 구한다.
# [2] 문제의 해법을 찾는데 결정적이었던 깨달음은 무엇이었는지
# 트라이 구조 / 트라이 구조 만들 때 지나치는 노드의 count dict(단어 개수에 따라) / 뒤집은 형태의 trie
# [3] (+한번에 맞추지 못한 경우 오답 원인 적기)
# ?가 접두사나 접미사로만 있다는 것을 나중에 봄 => 이에 따른 최적화해줌
#
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.word = False
        self.count = defaultdict(int)
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            node.count[len(word)] += 1
            node = node.children[c]
        node.word = True

    def startswith(self, word):
        node = self.root
        for c in word:
            if c == "?":
                return node.count[len(word)]
            else:
                if c in node.children:
                    node = node.children[c]
                else:
                    return 0
        return -1


def solution(words, queries):
    trie = Trie()
    reverse_trie = Trie()
    for word in words:
        trie.insert(word)
        reverse_trie.insert(word[::-1])
    res = []
    for query in queries:
        if query[0] != "?":
            res.append(trie.startswith(query))
        else:
            res.append(reverse_trie.startswith(query[::-1]))
    return res


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
