class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(nums) * len(nums[0]) != r * c: return nums
        num_reshape = [num for rows in nums for num in rows]
        res = [[0]*c for _ in range(r)]
        for ide, element in enumerate(num_reshape):
            i = 0 if ide < c else ide // c
            j = ide if ide < c else ide - i * c
            res[i][j] = element
        return res

