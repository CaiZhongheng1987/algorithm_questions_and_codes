# 冒泡排序
# 最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
# 最坏时间复杂度：O(n^2)
# 稳定性：稳定


def bubble_sort(nums):
    len_nums = len(nums)
    exchange_flag = 0
    idx = len_nums - 2

    while idx >= 0:
        for exchange_idx in range(idx+1):
            if nums[exchange_idx] > nums[exchange_idx+1]:
                nums[exchange_idx], nums[exchange_idx+1] = nums[exchange_idx+1], nums[exchange_idx]
                exchange_flag = 1

        if exchange_flag == 0:
            break
        else:
            exchange_flag = 0

        idx -= 1

    return None


input_list = [54, 26, 93, 77, 44, 31, 44, 55, 20]
print('原列表为： %s' % input_list)
bubble_sort(input_list)
print('新列表为： %s' % input_list)


