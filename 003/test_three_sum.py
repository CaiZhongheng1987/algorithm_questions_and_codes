# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums):
        nums.sort()
        sum_list = []
        for idx in range(0, len(nums)-2):
            if idx != 0 and nums[idx] == nums[idx-1]:
                continue
            else:

                l_idx = idx + 1
                r_idx = len(nums)-1

                while l_idx < r_idx:
                    sum_out = nums[idx] + nums[l_idx] + nums[r_idx]
                    if sum_out == 0:
                        sum_list.append([nums[idx], nums[l_idx], nums[r_idx]])
                        l_idx = l_idx + 1
                        r_idx = r_idx - 1
                        while nums[l_idx - 1] == nums[l_idx] and l_idx < r_idx:
                            l_idx = l_idx + 1

                        while nums[r_idx + 1] == nums[r_idx] and l_idx < r_idx:
                            r_idx = r_idx - 1

                    elif sum_out < 0:
                        l_idx = l_idx + 1
                        while nums[l_idx - 1] == nums[l_idx] and l_idx < r_idx:
                            l_idx = l_idx + 1
                    else:
                        r_idx = r_idx - 1
                        while nums[r_idx + 1] == nums[r_idx] and l_idx < r_idx:
                            r_idx = r_idx - 1



        # 穷举法，在leetcode里面会判定为超时
        # nums.sort()
        # sum_list = []
        # for begin_idx in range(0, len(nums) - 2):
        #     if begin_idx != 0 and nums[begin_idx] == nums[begin_idx - 1]:
        #         continue
        #     else:
        #         for end_idx in range(begin_idx + 1, len(nums)):
        #             if (end_idx != (begin_idx + 1)) and nums[end_idx] == nums[end_idx - 1]:
        #                 continue
        #             else:
        #                 target_value = - nums[begin_idx] - nums[end_idx]
        #                 if target_value in nums[end_idx + 1:]:
        #                     sum_list.append([nums[begin_idx], nums[end_idx], target_value])

        return sum_list


test_list = [0, 0, 0]  # [-1,0,1,2,-1,-4]  # [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]

my_solution = Solution

return_list = my_solution.threeSum(my_solution, test_list)
print(return_list)


