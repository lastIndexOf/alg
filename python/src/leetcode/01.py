"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
"""


# class Solution:
#     def twoSum(self, nums, target):
#         i, j, length = 0, 1, len(nums)

#         while i < length:
#             while j < length:
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#                 j += 1
#             i += 1
#             j = i + 1

class Solution:
    def twoSum(self, nums, target):
        for num in nums:
            i = nums.index(num)
            rest = target - num
            rest_l = nums[i+1:]
            if rest in rest_l:
                return [i, rest_l.index(rest)+i+1]
            del rest_l


s = Solution()
l = [3, 3]

print(l)
print(s.twoSum(l, 6))
