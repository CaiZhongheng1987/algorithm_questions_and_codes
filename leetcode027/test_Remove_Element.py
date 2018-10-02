# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
#
# 示例 1:
#
# 给定 nums = [3,2,2,3], val = 3,
#
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
#
# 你不需要考虑数组中超出新长度后面的元素。
# 示例 2:
#
# 给定 nums = [0,1,2,2,3,0,4,2], val = 2,
#
# 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
#
# 注意这五个元素可为任意顺序。
#
# 你不需要考虑数组中超出新长度后面的元素。


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        r_idx = 0
        for tmp_num in nums:
            if tmp_num != val:
                nums[r_idx] = tmp_num
                r_idx += 1

        return r_idx


# main test script
list_1 = [1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 6, 7]
val_1 = 1
my_test = Solution()

new_list = my_test.removeElement(list_1, val_1)
print(new_list)
print(list_1)
