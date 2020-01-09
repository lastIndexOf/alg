"""将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。"""
from functools import reduce


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 0:
            return ''

        path = ['' for _ in range(numRows)]
        x = 0

        dire = True
        for i in range(len(s)):
            path[x] += s[i]

            if dire:
                if x + 1 < numRows:
                    x += 1
                else:
                    x -= 1
                    dire = False
            else:
                if x - 1 < 0:
                    x += 1
                    dire = True
                else:
                    x -= 1

        return reduce(lambda a, b: a + b, path)


s = Solution()

print(s.convert('LEETCODEISHIRING', 3))
print(s.convert('LEETCODEISHIRING', 4))
