# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
#
# 注意：
#
# 答案中不可以包含重复的四元组。
#
# 示例：
#
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
#
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        sum_list = []

        for first_idx in range(0, len(nums) - 3):
            if nums[first_idx] > target and nums[first_idx] > 0:
                break

            if first_idx != 0 and nums[first_idx] == nums[first_idx - 1]:
                continue
            else:
                for idx in range(first_idx + 1, len(nums) - 2):
                    if (nums[first_idx] + nums[idx]) > target and (nums[first_idx] + nums[idx]) > 0:
                        break

                    if idx != (first_idx + 1) and nums[idx] == nums[idx - 1]:
                        continue
                    else:

                        l_idx = idx + 1
                        r_idx = len(nums) - 1

                        while l_idx < r_idx:
                            if (nums[first_idx] + nums[idx] + nums[l_idx]) > target and (nums[first_idx] + nums[idx] + nums[l_idx]) > 0:
                                break

                            sum_out = nums[first_idx] + nums[idx] + nums[l_idx] + nums[r_idx]
                            if sum_out - target == 0:
                                sum_list.append([nums[first_idx], nums[idx], nums[l_idx], nums[r_idx]])
                                l_idx = l_idx + 1
                                r_idx = r_idx - 1
                                while nums[l_idx - 1] == nums[l_idx] and l_idx < r_idx:
                                    l_idx = l_idx + 1

                                while nums[r_idx + 1] == nums[r_idx] and l_idx < r_idx:
                                    r_idx = r_idx - 1

                            elif sum_out - target < 0:
                                l_idx = l_idx + 1
                                while nums[l_idx - 1] == nums[l_idx] and l_idx < r_idx:
                                    l_idx = l_idx + 1
                            else:
                                r_idx = r_idx - 1
                                while nums[r_idx + 1] == nums[r_idx] and l_idx < r_idx:
                                    r_idx = r_idx - 1

        return sum_list


test_list = [1,-2,-5,-4,-3,3,3,5]
target = -11

my_solution = Solution()

return_list = my_solution.fourSum(test_list, target)
print(return_list)
