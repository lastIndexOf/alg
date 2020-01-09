class Solution:
    def maxArea(self, height: list) -> int:
        '''暴力解法'''
        max_area = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                w = j - i
                h = min(height[i], height[j])

                max_area = max_area if max_area > w * h else w * h

        return max_area

    def maxArea2(self, height: list) -> int:
        max_area = 0
        max_height = 0
        max_x = len(height) - 1
        last_height = height[max_x]

        for i in range(len(height) - 1):
            current_height = height[i]
            current_max_area = 0
            if current_height < max_height:
                continue

            if last_height >= current_height:
                current_max_area = (max_x - i) * current_height
            else:
                current_max_area = (max_x - i) * last_height
                index = max_x - 1
                while index > i:
                    if height[index] > last_height:
                        value = 0
                        if current_height > height[index]:
                            value = (index - i) * height[index]
                        else:
                            value = (index - i) * current_height
                            current_max_area = value if value > current_max_area else current_max_area
                            break
                        current_max_area = value if value > current_max_area else current_max_area
                    index -= 1

            if max_area < current_max_area:
                max_area = current_max_area
                max_height = current_height

        return max_area

    def maxArea3(self, height: list) -> int:
        '''双指针法'''
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            temp_area = (right - left) * min((height[left], height[right]))
            max_area = max_area if max_area > temp_area else temp_area
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area


s = Solution()
print(s.maxArea([1, 2, 3, 4, 5, 25, 24, 3, 4]))
print(s.maxArea2([1, 2, 3, 4, 5, 25, 24, 3, 4]))
print(s.maxArea3([1, 2, 3, 4, 5, 25, 24, 3, 4]))
