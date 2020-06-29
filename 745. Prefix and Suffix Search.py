from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        self.a ={}
        for ind, i in enumerate(words):
            for j in range(len(i) + 1):
                for k in range(len(i) + 1):
                    now = i[:j] + '$' + i[k:]
                    self.a[now] = ind


    def f(self, prefix: str, suffix: str) -> int:
        k = prefix + '$' + suffix
        return self.a.get(k, -1)

if __name__ == '__main__':
    words = ["apple"]
    prefix = "a"
    suffix = "e"
    obj = WordFilter(words)
    print(obj.f(prefix, suffix))
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)