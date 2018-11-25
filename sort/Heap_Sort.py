# 堆排序
# 最优时间复杂度：O(nlog2(n))
# 最坏时间复杂度：O(nlog2(n))
# 稳定性：不稳定


def heap_sort(nums):
    # 创建最大堆
    len_nums = len(nums)
    for idx in range((len_nums-1)//2, -1, -1):
        heap_shift(nums, idx, len_nums-1)

    # 对最大堆进行调整，每次将第一个数和堆末尾的数进行交换，然后在对堆进行调整
    for heap_end_idx in range(len_nums-1, -1, -1):
        nums[heap_end_idx], nums[0] = nums[0], nums[heap_end_idx]
        heap_shift(nums, 0, heap_end_idx-1)

    return None


def heap_shift(nums, heap_start, heap_end):
    father_node = heap_start
    while True:
        child_node = 2*father_node + 1
        if child_node > heap_end:
            # 超出数组范围，就直接停止
            break

        if child_node+1 <= heap_end and nums[child_node+1] > nums[child_node]:
            # 在数组范围内，寻找两个子节点里面值最大的节点
            child_node += 1

        if nums[father_node] < nums[child_node]:
            # 如果父节点小于子节点，那就交换两个节点，并且将父节点的idx变为子节点的idx，一直循环下去
            nums[father_node], nums[child_node] = nums[child_node], nums[father_node]
            father_node = child_node
        else:
            break

    return None


input_list = [54, 26, 93, 77, 44, 31, 44, 55, 20]
print('原列表为： %s' % input_list)
heap_sort(input_list)
print('新列表为： %s' % input_list)
