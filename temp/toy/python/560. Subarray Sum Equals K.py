class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        store = dict()
        store[0]  = 1
        presum = 0
        count = 0
        for num in nums:
            presum += num
            if presum - k in store:
                count += store[presum - k]
            if presum in store:
                store[presum] += 1
            else: store[presum] = 1
        return count
