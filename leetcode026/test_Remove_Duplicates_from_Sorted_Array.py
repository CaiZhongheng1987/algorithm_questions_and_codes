# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 示例 1:
#
# 给定数组 nums = [1,1,2],
#
# 函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
#
# 给定 nums = [0,0,1,1,1,2,2,3,3,4],
#
# 函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
#
# 你不需要考虑数组中超出新长度后面的元素。


class Solution:
    def removeDuplicates(self, nums):
        len_nums = len(nums)
        if len_nums in [0, 1]:
            return len_nums

        l_idx = 1
        for idx in range(len_nums-1):
            if nums[idx+1] != nums[idx]:
                nums[l_idx] = nums[idx+1]
                l_idx += 1

        return l_idx



    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums in [0, 1]:
            return len_nums

        fst_idx = 1
        sec_idx = 1

        while sec_idx < len_nums:
            if nums[fst_idx-1] < nums[sec_idx]:
                nums[fst_idx] = nums[sec_idx]
                fst_idx += 1
                sec_idx += 1
            elif nums[fst_idx] == nums[sec_idx] and nums[fst_idx-1] < nums[fst_idx]:
                sec_idx += 1
            else:
                sec_idx += 1

        return fst_idx


# main test script
list_1 = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7]

my_test = Solution()

len_new_list = my_test.removeDuplicates(list_1)
print(list_1)
print(len_new_list)
