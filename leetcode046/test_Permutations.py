# 给定一个没有重复数字的序列，返回其所有可能的全排列。
#
# 示例:
#
# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
import copy


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
#         思路并不难想，这里可以用递归，也可以直接上for循环。
#         假设我们已经获得了n个数的全排列，那么n+1个数的全排列就是将第n个元素依次插入n+1个位置中。
#         假设我们已经获得两个元素的全排列[1, 2], [2, 1]，然后我们现在加入3这个元素
#         那么新的全排列就是将3放入1的前面，1和2的中间，2的后面，这三种方法。对于[2, 1]的情况，以此类推

        len_nums = len(nums)
        if len_nums == 0:
            return [[]]

        if len_nums == 1:
            return [[nums[0]]]

        out_list = [[]]
        for idx in range(0, len_nums):
            store_list = copy.deepcopy(out_list)
            new_list = []
            for insert_idx in range(0, idx+1):
                tmp_list = copy.deepcopy(store_list)
                for list_value in tmp_list:
                    list_value.insert(insert_idx, nums[idx])

                new_list.extend(tmp_list)

            out_list = copy.deepcopy(new_list)

        return out_list


input_list = [2, 3, 1, 4]

my_test = Solution()
result_list = my_test.permute(input_list)
print(result_list)
