class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        res = set([''])
        longest = ''
        for word in words:
            if word[:-1] in res:
                res.add(word)
                if len(word) > len(longest):
                    longest = word
        return longest