class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lindex = {c:i for i, c in enumerate(S)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(S):
            j = max(j, lindex[c])
            if i == j:
                ans.append(j-anchor + 1)
                anchor = j+1
        return ans

if __name__ == '__main__':
    print(Solution().partitionLabels(
        "ababcbacadefegdehijhklij"
    ))
