# 给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
#
# 返回被除数 dividend 除以除数 divisor 得到的商。
#
# 示例 1:
#
# 输入: dividend = 10, divisor = 3
# 输出: 3
# 示例 2:
#
# 输入: dividend = 7, divisor = -3
# 输出: -2
# 说明:
#
# 被除数和除数均为 32 位有符号整数。
# 除数不为 0。
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return None

        pos = ((dividend > 0) == (divisor > 0))
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor is 1:
            if pos is False:
                return min(2 ** 31 - 1, max(-1 * dividend, -2 ** 31))
            else:
                return min(2 ** 31 - 1, max(dividend, -2 ** 31))

        result = 0
        tmp_dividend = dividend
        tmp_divisor = divisor
        while tmp_dividend >= tmp_divisor:
            result, tmp_dividend = Solution.sub_divide(self, tmp_dividend, tmp_divisor, result)

        if pos is False:
            result *= -1

        return min(2**31-1, max(result, -2**31))

    def sub_divide(self, dividend, divisor, result):
        tmp_divisor = divisor
        # tmp_dividend = dividend
        tmp_index = 1
        while dividend >= tmp_divisor:
            tmp_index <<= 1
            tmp_divisor <<= 1

        tmp_divisor >>= 1
        tmp_index >>= 1
        result += tmp_index
        new_dividend = dividend - tmp_divisor
        return result, new_dividend


# main test script
nums_1 = -2000
nums_2 = 5
my_test = Solution()

return_result = my_test.divide(nums_1, nums_2)
print(return_result)
print(int(nums_1/nums_2))
