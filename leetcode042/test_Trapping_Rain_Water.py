# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
#
#
#
# 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。
#
# 示例:
#
# 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height is []:
            return 0

        len_height = len(height)
        left_idx = 0
        right_idx = len_height - 1
        sec_height = 0
        result_area = 0
        while left_idx < right_idx:
            if height[left_idx] < height[right_idx]:
                sec_height = max(sec_height, height[left_idx])
                result_area = result_area + sec_height - height[left_idx]
                left_idx += 1
            else:
                sec_height = max(sec_height, height[right_idx])
                result_area = result_area + sec_height - height[right_idx]
                right_idx -= 1

        return result_area


# main test script
test_list = [0,1,0,2,1,0,1,3,2,1,2,1]

my_test = Solution()
out_num = my_test.trap(test_list)
print(out_num)
