from typing import re


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = re.findall(r"\w+", paragraph.lower())
        return paragraph

if __name__ == '__main__':
    print(Solution().mostCommonWord(
        "Bob hit a ball, the hit BALL flew far after it was hit.",
        ["hit"]
    ))