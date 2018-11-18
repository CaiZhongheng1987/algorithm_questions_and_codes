# 希尔排序
# 最优时间复杂度：O(n)
# 最坏时间复杂度：O(n^2)
# 稳定性：不稳定


def shell_sort(nums):
    # 按照二分法来设计步长
    len_nums = len(nums)
    step = len_nums // 2  # 设定初始步长

    while step > 0:
        for idx in range(step):
            nums[idx::step] = insertion_sort(nums[idx::step])
        step = step // 2

    return None


def insertion_sort(sub_nums):
    len_sub_nums = len(sub_nums)
    for sorted_idx in range(1, len_sub_nums):
        for idx in range(sorted_idx-1, -1, -1):
            if sub_nums[idx] > sub_nums[idx+1]:
                sub_nums[idx], sub_nums[idx+1] = sub_nums[idx+1], sub_nums[idx]
            else:
                break

    return sub_nums


input_list = [54, 26, 93, 77, 44, 31, 44, 55, 20]
print('原列表为： %s' % input_list)
shell_sort(input_list)
print('新列表为： %s' % input_list)
