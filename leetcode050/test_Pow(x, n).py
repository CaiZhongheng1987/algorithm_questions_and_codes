# 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
#
# 示例 1:
#
# 输入: 2.00000, 10
# 输出: 1024.00000
# 示例 2:
#
# 输入: 2.10000, 3
# 输出: 9.26100
# 示例 3:
#
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2^-2 = 1/2^2 = 1/4 = 0.25
# 说明:
#
# -100.0 < x < 100.0
# n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
import math


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        # 采用类似于打淘汰赛的方式，将n进行分解，这样原来需要o(n)的乘法可以降为log2(n)
        if n is 0:
            return 1

        if n is 1:
            return x

        tmp_n = abs(n)
        pow_out = 1

        while tmp_n >= 1:
            # 计算当前的数为2的多少次幂
            tmp_val = math.floor(math.log(tmp_n, 2))
            tmp_pow_out = x
            # 用淘汰赛的方式计算这一轮的结果
            for _ in range(0, tmp_val):
                tmp_pow_out *= tmp_pow_out

            # 将这一轮的结果乘到最终结果上
            pow_out *= tmp_pow_out
            # 更新tmp_n
            tmp_n -= 2**tmp_val

        if n < 0:
            # 处理负数幂的情况
            pow_out = 1 / pow_out

        return pow_out


input_x = 3.2
input_n = -3

my_test = Solution()
my_out = my_test.myPow(input_x, input_n)
python_out = input_x**input_n
print(python_out-my_out)
