class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = dict()
        store[0]  = 1
        presum = 0
        count = 0
        for num in nums:
            presum += num
            if store[presum - k]:
                count += store[presum - k]
            if num in store:
                store[num] += 1
            else: store[num] = 1
        return count
