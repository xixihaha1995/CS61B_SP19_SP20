from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray = dict()
        gray[0] = ['0']
        gray[1] = ['0' , '1']
        for i in range(2, n+1):
            n_gray= []
            for pre in gray[i-1]:
                n_gray.append('0' + pre)
            for pre in gray[i-1][::-1]:
                n_gray.append('1' + pre)
            gray[i] = n_gray
        # return map(lambda x : int(x,2), gray[n])
        return gray[n]

if __name__ == '__main__':
    print(
        Solution().grayCode(3)
    )

