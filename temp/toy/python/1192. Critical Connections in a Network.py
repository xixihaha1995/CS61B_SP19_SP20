from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        severDict = dict()
        ans =[]
        for sea, seb in connections:
            for se in [sea, seb]:
                if se not in severDict:
                    severDict[se] = 1
                else:
                    severDict[se] += 1
                    if [sea,seb] in ans:
                        ans.remove([sea,seb])
            ans.append([sea,seb])

        return ans

if __name__ == '__main__':
    print(Solution().criticalConnections(
       4, [[0, 1], [1, 2], [2, 0], [1, 3]]
    ))