# 选择排序
# 最优时间复杂度：O(n*n)
# 最坏时间复杂度：O(n*n)
# 稳定性：不稳定


def selection_sort(nums):
    len_nums = len(nums)
    for sorted_idx in range(len_nums):
        min_idx = sorted_idx
        for idx in range(sorted_idx+1, len_nums):
            if nums[idx] < nums[min_idx]:
                min_idx = idx

        nums[sorted_idx], nums[min_idx] = nums[min_idx], nums[sorted_idx]

    return None


input_list = [54, 26, 93, 77, 44, 31, 44, 55, 20]
print('原列表为： %s' % input_list)
selection_sort(input_list)
print('新列表为： %s' % input_list)

