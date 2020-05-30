import collections


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadset = set(deadends)
        if target in deadends: return -1
        visited = set()
        visited.add(["0000"])
        q = collections.deque()
        q.append("0000")
        step = 0
        while q:
            size = len(q)
            step += 1
            for i in range(size):
                point = q.popleft()
                for j in range(4):

                    for k in range(-1,2,2):
                        newpoint = [i for i in point]
                        newpoint[j] = chr((ord(newpoint[j]-ord('0')+k + 10)) % 10 + ord('0'))
                        newpoint = "".join(newpoint)
                        if newpoint == target:
                            return step
                        if newpoint in deadset or newpoint in visited:
                            continue
                        q.append(newpoint)
                        visited.add(newpoint)
        return -1



