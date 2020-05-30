class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        q = collections.deque()
        q.append((beginWord, 1))
        while q:
            curr = q.popleft()
            currword = curr[0]
            currlen = curr[1]
            if currword == endWord: return currlen
            for i in range(len(currword)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    part1 = currword[: i]
                    part2 = currword[i + 1:]

                    nextword = part1 + j + part2
                    if nextword in wordset and nextword != currword:
                        wordset.remove(nextword)
                        q.append((nextword, currlen+1))
        return 0