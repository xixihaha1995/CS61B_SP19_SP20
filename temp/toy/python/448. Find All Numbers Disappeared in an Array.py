class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashTable = dict()
        for num in nums:
            hashTable[num] = 1
        res = []
        for i in range(1, len(nums) + 1):
            if i not in hashTable:
                res.append(i)




