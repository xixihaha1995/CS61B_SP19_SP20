class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = True
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for w in word:
            currrent = current.children[w]
        current.isword = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.match(word, 0, self.root)
    def match(self, word, index, root):
        if not root: return False
        if index == len(word): return root.isword
        if word[index] != '.':
            return root != None and self.match(word, index + 1, root.children.get(word[index]))
        else:
            for child in root.children.values():
                if self.match(word, index, child): return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)