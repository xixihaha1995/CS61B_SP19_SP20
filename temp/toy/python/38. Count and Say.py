class Solution:
    def countAndSay(selfs, n: int ) -> str:
        return "1"

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