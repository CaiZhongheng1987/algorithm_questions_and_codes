# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
# 示例:
#
# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
# 说明:
#
# 假设你总是可以到达数组的最后一个位置。


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
#         通过贪心算法来进行推导，
#         在当前位置a计算每次能够跳跃的最大位置b，然后统计a和b之间下一次能够跳跃的最大距离
#         由此得到下一次跳跃的局部最远距离和最大位置，持续更新
        idx = 0
        local_max_distance = 0
        local_max_idx = 0
        step_num = 0
        len_nums = len(nums)
        while idx != len_nums - 1:
            # 下一步可以走的idx范围为range(idx+1, min(nums[idx]+idx+1, len_nums))
            # 这个范围除去自身，也保证不超过数组本身的长度
            if nums[idx]+idx+1 >= len_nums:
                # 说明这一步就可以直接走到数组末尾
                step_num += 1
                break
            # 在这个范围内计算每个idx下一步可以走的最远的范围
            for tmp_idx in range(idx+1, min(nums[idx]+idx+1, len_nums)):
                # 计算范围内每个idx最远可以走到多远，并找到当中走得最远的idx，记录下来
                tmp_distance = nums[tmp_idx]+tmp_idx
                if tmp_distance > local_max_distance:
                    local_max_distance = tmp_distance
                    local_max_idx = tmp_idx

            # 选择可以走的最远的一步，更新idx，增加一步
            idx = local_max_idx
            step_num += 1
            local_max_distance = 0

        return step_num


input_list = [2, 3, 1, 1, 4]

my_test = Solution()
result = my_test.jump(input_list)
print(result)
