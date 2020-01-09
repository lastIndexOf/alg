"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''暴力法'''
        max_len, result = 0, ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                st = s[i:j]
                rev = st[::-1]

                if st == rev and len(st) > max_len:
                    max_len = len(st)
                    result = str(st)

        return result

    def longestPalindrome2(self, s: str) -> str:
        '''中心扩展'''
        max_len, result = 0, ''
        for center in range(len(s)):
            st = s[center]

            temp_len = 1
            temp_str = st
            left = center - 1
            right = center + 1

            while right < len(s) and s[right] == st:
                '''xyzAAAAAzyx的形式'''
                temp_len += 1
                temp_str += s[right]
                right += 1

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    temp_len += 2
                    temp_str = s[left] + temp_str + s[right]
                    left -= 1
                    right += 1
                else:
                    break

            max_len = max_len if max_len > temp_len else temp_len
            result = result if max_len > temp_len else temp_str

        return result


s = Solution()

# print(s.longestPalindrome2("ukxidnpsdfwieixhjnannbmtppviyppjgbsludrzdleeiydzawnfmiiztsjqqqnthwinsqnrhfjxtklvbozkaeetmblqbxbugxycrlzizthtuwxlmgfjokhqjyukrftvfwikxlptydybmmzdhworzlaeztwsjyqnshggxdsjrzazphugckgykzhqkdrleaueuajjdpgagwtueoyybzanrvrgevolwssvqimgzpkxehnunycmlnetfaflhusauopyizbcpntywntadciopanyjoamoyexaxulzrktneytynmheigspgyhkelxgwplizyszcwdixzgxzgxiawstbnpjezxinyowmqsysazgwxpthloegxvezsxcvorzquzdtfcvckjpewowazuaynfpxsxrihsfswrmuvluwbdazmcealapulnahgdxxycizeqelesvshkgpavihywwlhdfopmmbwegibxhluantulnccqieyrbjjqtlgkpfezpxmlwpyohdyftzgbeoioquxpnrwrgzlhtlgyfwxtqcgkzcuuwagmlvgiwrhnredtulxudrmepbunyamssrfwyvgabbcfzzjayccvvwxzbfgeglqmuogqmhkjebehtwnmxotjwjszvrvpfpafwomlyqsgnysydfdlbbltlwugtapwgfnsiqxcnmdlrxoodkhaaaiioqglgeyuxqefdxbqbgbltrxcnihfwnzevvtkkvtejtecqyhqwjnnwfrzptzhdnmvsjnnsnixovnotugpzuymkjplctzqbfkdbeinvtgdpcbvzrmxdqthgorpaimpsaenmnyuyoqjqqrtcwiejutafyqmfauufwripmpcoknzyphratopyuadgsfrsrqkfwkdlvuzyepsiolpxkbijqw"))  # cbbd
print(s.longestPalindrome2("aaa"))  # cbbd
#                         'sdabab'      dbbc
# print(s.longestPalindrome('cbbd'))
