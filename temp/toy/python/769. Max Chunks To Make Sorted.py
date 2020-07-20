class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        temp = float('-inf')

        for i in len(arr):
            temp = max(temp, arr[i])
            if i == temp: res += 1
        return res
