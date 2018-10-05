# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
# 你可以假设数组中无重复元素。
#
# 示例 1:
#
# 输入: [1,3,5,6], 5
# 输出: 2
# 示例 2:
#
# 输入: [1,3,5,6], 2
# 输出: 1
# 示例 3:
#
# 输入: [1,3,5,6], 7
# 输出: 4
# 示例 4:
#
# 输入: [1,3,5,6], 0
# 输出: 0


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            # 空数组的话直接插入target就行了
            return 0

        len_nums = len(nums)

        if target <= nums[0]:
            return 0

        if target > nums[-1]:
            return len_nums

        left_idx = 0
        right_idx = len_nums - 1
        mid_idx = 0
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] > target:
                # 确定在左边区域
                right_idx = mid_idx - 1
            else:
                # 确定在右边区域
                left_idx = mid_idx + 1

        # 到这一步，说明数组中没有target
        if nums[mid_idx] > target:
            return mid_idx
        else:
            return mid_idx+1


# main test script
test_list = [1, 3, 5, 7, 8]
target = 0
my_test = Solution()

return_result = my_test.searchInsert(test_list, target)
print(return_result)
