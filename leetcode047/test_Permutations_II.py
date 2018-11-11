# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 和上一道题思路一样，只是每次append的时候判断是否重复，如果有重复的就不append了
        ans = []
        len_nums = len(nums)
        if len_nums == 1:
            return [nums]
        if len_nums == 0:
            return [[]]
        ans1 = self.permuteUnique(nums[1:])
        b = nums[0]
        len_ans1 = len(ans1)
        for i in range(len_nums):
            for j in range(len_ans1):
                str1 = []
                str1 += ans1[j][:i]
                str1 += [b]
                str1 += ans1[j][i:]
                if str1 not in ans:
                    ans.append(str1)

        return ans


input_list = [2, 1, 1]

my_test = Solution()
result_list = my_test.permuteUnique(input_list)
print(result_list)
