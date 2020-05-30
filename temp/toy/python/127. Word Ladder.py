class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = []
        q.append((beginWord, 1))
        while q:
            curr = q.pop()
            currword = curr[0]
            currlen = curr[1]
            for i in range(len(currword)):
                if currword == endWord: return currlen
                part1 = currword[ : i]
                part2 = currword[i+1 : ]
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if j != currword[i]:
                        nextword = part1 + j + part2
                        if nextword in wordList:
                            wordList.remove(nextword)
                            q.append((nextword, currlen+1))


