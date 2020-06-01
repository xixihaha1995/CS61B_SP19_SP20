class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                break
            elif sum < target:
                i += 1
            else: j -= 1
        return [i+1, j+1]