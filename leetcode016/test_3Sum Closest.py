# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
#
# 与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums, target):
        len_nums = len(nums)

        if len_nums <= 3:
            return sum(nums)

        nums.sort()
        close_sum = float("inf")

        for idx in range(len_nums-2):
            if idx != 0 and nums[idx] == nums[idx-1]:
                continue
            else:
                l_idx = idx + 1
                r_idx = len_nums - 1

                while l_idx < r_idx:
                    sum_out = nums[idx] + nums[l_idx] + nums[r_idx]

                    if sum_out-target == 0:
                        return sum_out
                    elif abs(sum_out-target) < abs(close_sum):
                        close_sum = sum_out-target
                        if sum_out < target:  # 说明当前的sum_out应该增加，继续寻找更接近的值
                            l_idx += 1
                            while nums[l_idx - 1] == nums[l_idx] and l_idx < r_idx:
                                l_idx += 1
                        else:  # 说明当前的sum_out应该减小，继续寻找更接近的值
                            r_idx -= 1
                            while nums[r_idx + 1] == nums[r_idx] and l_idx < r_idx:
                                r_idx -= 1
                    else:  # 说明当前的sum_out-target的绝对值应该减小
                        if sum_out > target:
                            r_idx -= 1
                            while nums[r_idx + 1] == nums[r_idx] and l_idx < r_idx:
                                r_idx -= 1
                        else:
                            l_idx += 1
                            while nums[l_idx - 1] == nums[l_idx] and l_idx < r_idx:
                                l_idx += 1

        return close_sum + target


test_list = [1,2,4,8,16,32,64,128]
test_target = 82

my_test = Solution()
out_sum = my_test.threeSumClosest(test_list, test_target)
print(out_sum)
