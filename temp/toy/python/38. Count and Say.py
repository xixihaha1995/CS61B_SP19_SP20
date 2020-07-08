class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        pre = self.countAndSay(n-1)
        result = ""
        count = 1
        for i in range(len(pre)):
            if i < (len(pre) -1) and pre[i] == pre[i+1]:
                count += 1
            else:
                if i == len(pre) - 1 and pre[i] != pre[i - 1]:
                    result = result + "1" + pre[-1]
                    break
                result = result + str(count) + pre[i]
                count = 1

        return result

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = int(line);

            ret = Solution().countAndSay(n)

            out = (ret);
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()