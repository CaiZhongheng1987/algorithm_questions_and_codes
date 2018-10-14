# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
#
# 示例 1:
#
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:
#
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 说明：
#
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
import numpy as np


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        if num1 == '1':
            return num2

        if num2 == '1':
            return num1

        # 大数相乘，将每个数分解为以10的整数次幂为底的向量，然后做卷积
        # 当中需要用到numpy，用来做卷积运算
        # 其实理论上来说还有更快的方法，那就是说将线性卷积改为等效的循环卷积，然后做FFT，不过这里就不装这个逼了

        # 先分解
        vector1 = list(map(int, list(num1)))
        vector2 = list(map(int, list(num2)))

        array1 = np.array(vector1)
        array2 = np.array(vector2)
        conv_out = np.convolve(array1, array2, mode='full')
        conv_out = conv_out.tolist()
        len_conv_out = len(conv_out)

        # 从10**0开始处理，目的是确保list里面每个元素都不超过10
        for idx in range(len_conv_out-1, 0, -1):
            tmp_val = conv_out[idx] // 10
            # 在循环过程中顺便把已经处理好的位数都转为字符类型，方便后面字符拼接
            conv_out[idx] = str(conv_out[idx] % 10)
            conv_out[idx-1] += tmp_val

        # 单独将list的第一个值转为字符类型
        conv_out[0] = str(conv_out[0])
        # 这样返回的时候直接字符串拼接起来就可以
        return ''.join(conv_out)


# main test script
test_num1 = '123'
test_num2 = '456'

my_test = Solution()
out_num = my_test.multiply(test_num1, test_num2)
print(out_num)
