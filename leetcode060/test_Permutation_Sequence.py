# 给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
#
# 按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 给定 n 和 k，返回第 k 个排列。
#
# 说明：
#
# 给定 n 的范围是 [1, 9]。
# 给定 k 的范围是[1,  n!]。
# 示例 1:
#
# 输入: n = 3, k = 3
# 输出: "213"
# 示例 2:
#
# 输入: n = 4, k = 9
# 输出: "2314"


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factor = list()
        factor.append(1)
        # 列出前n个数各自的阶乘，从0开始
        for idx in range(1, n):
            factor.append(factor[-1]*idx)

        result = ''
        k -= 1  # k需要减1是因为初始化序列就是第一个排列
        numbers = [i for i in range(1, n+1)]
        for i in range(n - 1, -1, -1):
            # 计算当前位是哪个数字，数字取自numbers数组
            number = k // factor[i]
            # 计算剩下的余数
            k %= factor[i]
            # 将这一位计算出来的数字转成字符，存入result中
            result += str(numbers[number])
            # 当前数字已被使用，就从numbers中删除
            del numbers[number]
        return result

    def getPermutation2(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        # 从小到大依次排序，排列到第k个就收手return
        k_idx = 1  # 初始的序列也算一个，所以k_idx初始化为1
        nums = [str(i) for i in range(1, n+1)]

        # 本题和leetcode031很类似，这里直接借用031的代码
        while k_idx < k:
            idx = n-1

            # 从末尾开始，寻找子list是否已经到达子list的最大
            while nums[idx] <= nums[idx - 1]:
                idx -= 1

            # 到这一步，相当于就从中间寻找下一个排列
            # 首先在后面的子list中寻找比nums[idx-1]刚好大一个排位的元素，
            # 即子list-nums[idx-1]后的最小值，考虑到子list是递减的，所以可以直接比大小
            c_idx = idx
            while c_idx < n:
                if nums[c_idx] > nums[idx - 1]:
                    c_idx += 1
                else:
                    break

            # 交换idx-1和寻找到的c_idx-1，再对剩下的子list进行reverse
            nums[idx - 1], nums[c_idx - 1] = nums[c_idx - 1], nums[idx - 1]
            tmp_nums = nums[idx:]
            nums[idx:] = tmp_nums[::-1]
            k_idx += 1

        tmp_string = ''.join(nums)
        return tmp_string


if __name__ == '__main__':
    input_n = 4
    input_k = 24
    my_test = Solution()
    out_string = my_test.getPermutation(input_n,input_k)
    print(out_string)
