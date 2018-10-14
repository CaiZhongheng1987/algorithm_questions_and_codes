# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
#
# 示例 1:
#
# 输入: [1,2,0]
# 输出: 3
# 示例 2:
#
# 输入: [3,4,-1,1]
# 输出: 2
# 示例 3:
#
# 输入: [7,8,9,11,12]
# 输出: 1
# 说明:
#
# 你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 既然只能用o(n)的复杂度，那那我们就遍历两次

        len_nums = len(nums)
        # 从第一个数开始，继续遍历，将所有在1~len_nums之间的整数排序到对应的idx-1上
        # 比如2就排序到idx=1的位置上，4就排序到idx=3的位置上
        for idx in range(len_nums):
            # 此处需要用while循环反复迭代，保证最后idx-1位置上的数就是idx
            # nums[nums[idx]-1] != nums[idx]的条件是指如果两边的数已经一致，再交换也无济于事
            while 0 < nums[idx] < len_nums and nums[nums[idx]-1] != nums[idx]:
                tmp_val = nums[idx]
                nums[idx], nums[tmp_val-1] = nums[tmp_val-1], nums[idx]
                # nums[idx], nums[nums[idx]-1] = nums[nums[idx]-1], nums[idx]

        # 第二次遍历
        # 寻找第一个nums[idx]不等于idx-1的数
        idx = 0
        while idx < len_nums:
            if nums[idx] != idx+1:
                break
            else:
                idx += 1

        # 遍历完成后，根据idx，说明缺失的最小正整数就是idx+1
        return idx+1


# main test script
test_list = [1, 1]

my_test = Solution()
out_num = my_test.firstMissingPositive(test_list)
print(out_num)
