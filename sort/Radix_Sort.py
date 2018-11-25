# 基数排序
# 最优时间复杂度：O(kn)
# 最坏时间复杂度：O(kn)
# 稳定性：稳定
import math


def radix_sort(nums, radix=10):
    # 计算nums数组中的数字可以用K位十进制数来表示
    K = int(math.ceil(math.log(max(nums)+1, radix)))

    # 接下来需要经历K次循环来排序
    for idx in range(1, K+1):
        # 既然是十进制，那就开一个数组，里面有十个元素
        bucket = [[] for idx in range(radix)]
        for val in nums:
            # 获得整数的第K位数字，按照第K位数字的大小进行排序
            bucket[val % (radix**idx) // (radix**(idx-1))].append(val)
        del nums[:]
        for each in bucket:
            # 做桶合并
            nums.extend(each)
    return None


input_list = [54, 26, 93, 77, 44, 31, 2, 7, 4, 44, 55, 20]
print('原列表为： %s' % input_list)
radix_sort(input_list)
print('新列表为： %s' % input_list)

