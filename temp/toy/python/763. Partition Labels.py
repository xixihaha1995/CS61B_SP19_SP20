class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        last = {c:i for i, c in enumerate(S)}
        anchor = j = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                ans.append(i-anchor + 1)
                anchor = i + 1
        return ans


if __name__ == '__main__':
    print(Solution().partitionLabels(
        "ababcbacadefegdehijhklij"
    ))
