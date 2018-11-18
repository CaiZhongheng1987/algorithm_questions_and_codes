# 归并排序
# 最优时间复杂度：O(nlog2(n))
# 最坏时间复杂度：O(nlog2(n))
# 稳定性：稳定


def merge_sort(nums):
    len_nums = len(nums)
    if len_nums <= 1:
        return nums

    mid_idx = len_nums // 2
    left_nums = merge_sort(nums[:mid_idx])
    right_nums = merge_sort(nums[mid_idx:])
    return merge(left_nums, right_nums)


def merge(left, right):
    merge_out = []
    while left and right:
        if left[0] < right[0]:
            merge_out.append(left.pop(0))
        else:
            merge_out.append(right.pop(0))

    if left:
        merge_out += left
    if right:
        merge_out += right

    return merge_out


input_list = [54, 26, 93, 77, 44, 31, 44, 55, 20]
print('原列表为： %s' % input_list)
output_list = merge_sort(input_list)
print('新列表为： %s' % output_list)
