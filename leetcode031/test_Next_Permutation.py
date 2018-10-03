# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 寻找list结束递增趋势的索引号
        len_nums = len(nums)
        if len_nums in [0, 1]:
            return

        idx = len_nums - 1
        # 从末尾开始，寻找子list是否已经到达子list的最大
        while nums[idx] <= nums[idx-1]:
            idx -= 1
            if idx == 0:
                # 说明已经到了最大的排列，那就直接sort并返回
                nums.reverse()
                return

        # 到这一步，相当于就从中间寻找下一个排列
        # 首先在后面的子list中寻找比nums[idx-1]刚好大一个排位的元素，
        # 即子list-nums[idx-1]后的最小值，考虑到子list是递减的，所以可以直接比大小
        c_idx = idx
        while c_idx < len_nums:
            if nums[c_idx] > nums[idx-1]:
                c_idx += 1
            else:
                break

        # 交换idx-1和寻找到的c_idx-1，再对剩下的子list进行reverse
        nums[idx-1], nums[c_idx-1] = nums[c_idx-1], nums[idx-1]
        tmp_nums = nums[idx:]
        nums[idx:] = tmp_nums[::-1]
        return


# main test script
test_list = [1, 3, 2]
my_test = Solution()

my_test.nextPermutation(test_list)
print(test_list)
