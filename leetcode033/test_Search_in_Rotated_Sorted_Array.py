# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 必须使用二分法
        if not nums:
            return -1

        len_nums = len(nums)
        left_idx = 0
        right_idx = len_nums-1
        while left_idx <= right_idx:
            mid_idx = int((right_idx + left_idx) / 2)
            if nums[mid_idx] == target:
                # 既然碰到了就直接返回
                return mid_idx
            if nums[mid_idx] != target and left_idx == right_idx:
                # 说明在该数组里面找不到和target相等的元素
                break

            # 首先要确定数组的循环旋转情况
            if target > nums[mid_idx]:
                # 分类讨论，确定target究竟在左半区域还是右半区域
                if nums[mid_idx] <= nums[right_idx]:
                    if nums[right_idx] >= target:
                        # 说明target在右半区域
                        left_idx = mid_idx + 1
                    else:
                        # 说明target在左半区域
                        right_idx = mid_idx - 1
                else:
                    # nums[mid_idx] > nums[right_idx]:
                    # 确定在右半区域
                    left_idx = mid_idx + 1
            else:
                # target < nums[mid_idx]:
                if nums[mid_idx] >= nums[left_idx]:
                    if nums[left_idx] <= target:
                        # 说明target在左半区域
                        right_idx = mid_idx - 1
                    else:
                        # 说明target在右半区域
                        left_idx = mid_idx + 1
                else:
                    # 确定在左半区域
                    right_idx = mid_idx - 1
        return -1


# main test script
test_list = [3, 1]
target = 1
my_test = Solution()

return_result = my_test.search(test_list, target)
print(return_result)
