"""给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_len = 0
        temp_len = 0
        start_index = 0
        hashmap = {}
        for index in range(0, len(s)):
            st = s[index]
            if st not in hashmap or start_index > hashmap[st]:
                hashmap[st] = index
                temp_len += 1
            else:
                max_len = max_len if max_len > temp_len else temp_len
                temp_len = index - hashmap[st]
                start_index = hashmap[st] + 1
                hashmap[st] = index

        return max_len if max_len > temp_len else temp_len


s = Solution()

print(s.lengthOfLongestSubstring('tmmzuxt'))
print(s.lengthOfLongestSubstring('arabcacfr'))
