# 给定n个非负整数a1，a2，...，an，每个数代表坐标中的一个点(i, ai) 。在坐标内画n条垂直线，垂直线i的两个端点分别为(i, ai)和(i, 0)。找出其中的两条线，使得它们与x轴共同构成的容器可以容纳最多的水。
#
# 说明：你不能倾斜容器，且n的值至少为2。
#
#
# 图中垂直线代表输入数组[1, 8, 6, 2, 5, 4, 8, 3, 7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为49。
#
# 示例:
#
# 输入: [1, 8, 6, 2, 5, 4, 8, 3, 7]
#
# 输出: 49


class Solution:
    def maxArea(self, height):
        # 采用左右双指针移动的方法，每次移动较短边的idx
        len_h = len(height)
        left_idx = 0
        right_idx = len_h - 1
        max_area = 0

        while left_idx != right_idx:
            if height[left_idx] >= height[right_idx]:
                tmp_area = height[right_idx] * (right_idx - left_idx)
                right_idx -= 1
            else:
                tmp_area = height[left_idx] * (right_idx - left_idx)
                left_idx += 1

            max_area = max(tmp_area, max_area)
            # print(max_area)

        return max_area


h_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]

my_test = Solution()
out_area = my_test.maxArea(h_list)
print(out_area)
