# 插入排序
# 最优时间复杂度：O(n)
# 最坏时间复杂度：O(n^2)
# 稳定性：稳定


def insertion_sort(nums):
    len_nums = len(nums)
    for sorted_idx in range(1, len_nums):
        for idx in range(sorted_idx-1, -1, -1):
            if nums[idx] > nums[idx+1]:
                nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
            else:
                break

    return None


input_list = [54, 26, 93, 77, 44, 31, 44, 55, 20]
print('原列表为： %s' % input_list)
insertion_sort(input_list)
print('新列表为： %s' % input_list)
