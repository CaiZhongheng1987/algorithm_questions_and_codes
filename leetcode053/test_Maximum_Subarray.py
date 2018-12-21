# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 使用动态规划方案，假设sub_sum[idx]是以idx为结尾的和最大的连续子序列之和，
        # 那么sub_sum[idx+1]就应该在sub_sum[idx]+nums[idx+1]和nums[idx+1]当中产生
        # 实际中只需要保存上一个idx的sub_sum即可，这样就可以节省很多空间
        len_nums = len(nums)
        if len_nums is 0:
            return None
        if len_nums is 1:
            return nums[0]

        last_sum = nums[0]
        cur_max_sum = nums[0]
        for idx in range(1, len_nums):
            if last_sum > 0:
                # 那就说明最大的连续子序列应该延长，包含当前的idx
                last_sum += nums[idx]
            else:
                # 那就说明最大的连续子序列应该就只有nums[idx]
                last_sum = nums[idx]
            # 更新当前最大的连续子序列之和
            cur_max_sum = max(cur_max_sum, last_sum)

        return cur_max_sum


input_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
my_test = Solution()
out_sum = my_test.maxSubArray(input_list)
print(out_sum)
