import collections
from typing import List


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dsu = DSU()
        em_to_name = dict()
        em_to_id = dict()
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                dsu.union(em_to_id[acc[1]], em_to_id[email])
        ans = collections.defaultdict(list)
        for email in em_to_name:
            ans[dsu.find(em_to_id[email])].append(email)
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]


class DSU:
    def __init__(self):
        self.par = list(range(10001))

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        self.par[self.find(x)] = self.find(y)


if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],

                ["John", "johnnybravo@mail.com"],

                ["Mary", "mary@mail.com"]]
    print(Solution().accountsMerge(
        accounts
    ))
