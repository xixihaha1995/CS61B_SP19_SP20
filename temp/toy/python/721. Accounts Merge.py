from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
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
                dsu.union(em_to_id[email], em_to_id[acc[1]])

        for email in em_to_name:
            ans = [dsu.find(em_to_id[email])].append(email)
        return ans


class DSU:
    def __init__(self):
        self.par = range(10001)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
            # self.par[self.find(x)] = self.find(x)
        return self.par[x]

    def union(self, x, y):
        # self.par[self.find(x)] = self.find(y)
        self.par[self.find(x)] = self.find(y)

    def same(self, x,y):
        return self.find(x) == self.find(y)

if __name__ == '__main__':
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],

                ["John", "johnnybravo@mail.com"],

                ["Mary", "mary@mail.com"]]
    print(Solution().accountsMerge(
        accounts
    ))