# 快速排序
# 最优时间复杂度：O(nlog2n)
# 最坏时间复杂度：O(n^2)
# 稳定性：不稳定


def quick_sort(nums, left, right):
    if left < right:
        middle = partition(nums, left, right)
        quick_sort(nums, left, middle-1)
        quick_sort(nums, middle+1, right)

    return None


def partition(nums, left, right):
    pivot = nums[right]
    store_idx = left
    for idx in range(left, right):
        if nums[idx] <= pivot:
            nums[store_idx], nums[idx] = nums[idx], nums[store_idx]
            store_idx += 1

    nums[store_idx], nums[right] = nums[right], nums[store_idx]

    return store_idx


input_list = [54, 26, 93, 77, 44, 31, 44, 55, 20]
print('原列表为： %s' % input_list)
quick_sort(input_list, 0, len(input_list)-1)
print('新列表为： %s' % input_list)
