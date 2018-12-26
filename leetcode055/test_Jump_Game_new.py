# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 从位置 0 到 1 跳 1 步, 然后跳 3 步到达最后一个位置。
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。


class Solution:
    def canJump(self, nums):
        # 这个方法简直是天秀，判断每个idx可以走到的最远的地方
        # 一旦idx已经达到最远的地方，而far还不能比当前的idx更大的话，那就说明这个idx就是0，而且到这里就走不下去了。
        far = 0
        for k, v in enumerate(nums):
            far = max(far, k+v)
            if far <= k and (k != len(nums)-1):
                return False
        return True

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 空列表直接返回False
        if not nums:
            return False
        # 如果列表全是正整数，那肯定能到达最后的位置
        if 0 not in nums:
            return True
        # 如果列表就是[0]，那肯定能到达最后的位置
        if nums == [0]:
            return True
        # 如果列表多于一个元素，且第一个元素就是0，那肯定没办法到达最后的位置
        if nums[0] is 0:
            return False
        # 将0作为分隔符，划分区间
        len_nums = len(nums)
        zero_list = [idx for idx, val in enumerate(nums) if val == 0]
        zero_list.insert(0, -1)
        zero_list.append(len_nums)
        # 通过for循环方式计算nums[idx]+idx的值，并与其下一个0元素所在的索引进行比较
        # 如果nums[idx]+idx > 0_idx，就说明这一段区间可以跳过去
        begin_idx = 0
        zero_idx = 1
        while 1:
            cur_max_idx = 0
            for idx in range(begin_idx, zero_list[zero_idx]):
                # 在两个0元素的区间内寻找可以跳到最远的idx
                cur_max_idx = max(cur_max_idx, nums[idx]+idx)
            # 进行判断，看cur_max_idx是否能够大于下一个zero_idx
            if cur_max_idx >= len_nums-1:
                # 直接就可以跳到结尾
                return True
            elif cur_max_idx <= zero_list[zero_idx]:
                # 说明连下一个区间都跳不过去
                return False
            else:
                # 说明可以跳到下一个或者下几个0元素区间，这里通过while循环来查找
                while cur_max_idx > zero_list[zero_idx+1]:
                    zero_idx += 1
                begin_idx = zero_list[zero_idx]+1  # 更新下一个0元素区间的起始值
                zero_idx += 1


if __name__ == '__main__':
    # input_list = [4, 0, 1, 0, 1, 0]
    # input_list = [3, 2, 1, 0, 4]
    input_list = [3,0,8,2,0,0,1]
    my_test = Solution()
    final_decision = my_test.canJump(input_list)
    print(final_decision)
