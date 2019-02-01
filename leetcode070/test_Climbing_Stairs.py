# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
#
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
from math import sqrt


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        # F(n+1) = F(n)+F(n-1)，这个问题实质是求解斐波那契数列
        # 根据通项公式可以直接计算
        n += 1
        val_0 = (1+sqrt(5))/2
        val_1 = (1-sqrt(5))/2
        return round(1/sqrt(5)*(val_0**n-val_1**n))


if __name__ == '__main__':
    input_n = 50
    my_test = Solution()
    return_nums = my_test.climbStairs(input_n)
    print(return_nums)

