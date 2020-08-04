from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count = 0
        for pos in range(len(flowerbed)):
            if flowerbed[pos] == 0 and (pos == 0 or flowerbed[pos-1] == 0) and (pos == len(flowerbed) - 1 or flowerbed[pos+1]==0):
                flowerbed[pos] = 1
                count += 1
            pos += 1
        return count >= n
