"""
给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        length = len(nums1) + len(nums2)
        target_index = length >> 1

        if not len(nums1):
            return nums2[target_index] if length % 2 != 0 else (
                nums2[target_index] + nums2[target_index - 1]) / 2

        if not len(nums2):
            return nums1[target_index] if length % 2 != 0 else (
                nums1[target_index] + nums1[target_index - 1]) / 2

        left_index, right_index = 0, 0
        ret = []
        index = 0
        while index <= target_index + 1:
            if left_index < len(nums1) and right_index < len(nums2):
                if nums1[left_index] < nums2[right_index]:
                    ret.append(nums1[left_index])
                    left_index += 1
                else:
                    ret.append(nums2[right_index])
                    right_index += 1
            elif left_index < len(nums1):
                ret.append(nums1[left_index])
                left_index += 1
            elif right_index < len(nums2):
                ret.append(nums2[right_index])
                right_index += 1
            else:
                break
            index += 1

        print(ret, target_index)
        return ret[target_index] if length % 2 != 0 else (ret[target_index] + ret[target_index - 1]) / 2


s = Solution()

print(s.findMedianSortedArrays([1], [1]))
