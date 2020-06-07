class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        letters = []
        nums = []
        for log in logs:
            logsplit = log.split(" ")
            if logsplit[1].isalpha():
                # letters.append((" ".join(logsplit[1:]), logsplit[0]))
                letters.append((" ".join(logsplit[1:]), logsplit[0]))
            else: nums.append(logsplit)
        letters.sort()
        return [letter[1] + " " + letter[0] for letter in letters ] + nums

if __name__ == '__main__':
    print(
        Solution().reorderLogFiles(
            ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
        )
    )