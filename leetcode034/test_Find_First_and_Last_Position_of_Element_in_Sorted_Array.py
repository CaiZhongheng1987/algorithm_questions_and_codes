# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        len_nums = len(nums)
        left_idx = 0
        right_idx = len_nums - 1
        mid_idx = 0
        # 首先判断数组中有没有target，用二分法
        while left_idx <= right_idx:
            mid_idx = (left_idx + right_idx) // 2
            if nums[mid_idx] == target:
                break
            elif nums[mid_idx] > target:
                # 在左边区域
                right_idx = mid_idx - 1
            else:
                # 在右边区域
                left_idx = mid_idx + 1

        # 循环结束时如果找不到target，那就返回return
        if nums[mid_idx] != target:
            return [-1, -1]

        # 走到这一步，就说明target存在，接下来继续使用二分法查找左边界和右边界
        out_list = [-1, -1]
        if nums[left_idx] == target:
            # 因为left_idx = mid_idx + 1， 而上一次的mid_idx不等于target
            # 所以本次的left_idx刚好就是target的左边界
            out_list[0] = left_idx

        if nums[right_idx] == target:
            # 同理，本次的right_idx刚好就是target的右边界
            out_list[1] = right_idx

        if out_list[0] == -1:
            # 说明上边界还没找到，继续用二分法查找
            low_idx = left_idx + 1
            high_idx = mid_idx
            while low_idx <= high_idx:
                new_mid_idx = (low_idx + high_idx) // 2
                if nums[new_mid_idx] == target and nums[new_mid_idx-1] != target:
                    out_list[0] = new_mid_idx
                    break
                elif nums[new_mid_idx] == target and nums[new_mid_idx-1] == target:
                    # 在左边区域
                    high_idx = new_mid_idx - 1
                else:
                    # 在右边区域
                    low_idx = new_mid_idx + 1

        if out_list[1] == -1:
            # 说明下边界还没找到，继续用二分法查找
            low_idx = mid_idx
            high_idx = right_idx - 1
            while low_idx <= high_idx:
                new_mid_idx = (low_idx + high_idx) // 2
                if nums[new_mid_idx] == target and nums[new_mid_idx+1] != target:
                    out_list[1] = new_mid_idx
                    break
                elif nums[new_mid_idx] == target and nums[new_mid_idx+1] == target:
                    # 在右边区域
                    low_idx = new_mid_idx + 1
                else:
                    # 在左边区域
                    high_idx = new_mid_idx - 1

        return out_list


# main test script
test_list = [5, 7, 7, 8, 8, 10]
target = 7
my_test = Solution()

return_list = my_test.searchRange(test_list, target)
print(return_list)
