# Leetcode

# 给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
#
# 你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]


def two_sum(nums, target):
    # 使用字典，一遍for循环
    new_dict = {}
    for idx in range(0, len(nums)):
        if (target - nums[idx]) in new_dict.keys() and new_dict[target - nums[idx]] != idx:
            return [idx, new_dict[target - nums[idx]]]
        else:
            new_dict[nums[idx]] = idx

    # 使用字典，两遍for循环
    # new_dict = {}
    # for idx in range(0, len(nums)):
    #     new_dict[nums[idx]] = idx
    #
    # for idx in range(0, len(nums)):
    #     if (target - nums[idx]) in new_dict.keys() and new_dict[target - nums[idx]] != idx:
    #         return [idx, new_dict[target - nums[idx]]]

    # 穷举法
    # for first_idx in range(0, len(nums) - 1):
    #     for second_idx in range(first_idx + 1, len(nums)):
    #         if target == (nums[first_idx] + nums[second_idx]):
    #             return [first_idx, second_idx]

    return


test_list = [3,3,11,15]
test_target = 6

return_idx = two_sum(test_list, test_target)
print(return_idx)
