# 给定一个 32 位有符号整数，将整数中的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。
# 根据这个假设，如果反转后的整数溢出，则返回 0。


class Solution:
    def reverse(self, x):
        sign = (x >= 0)
        abs_x = abs(x)
        num_str = str(abs_x)
        len_s = len(num_str)
        new_num = 0

        for idx in range(len_s-1, -1, -1):
            new_num = new_num + int(num_str[idx])*10**idx

        if sign is False:
            new_num = -1 * new_num

        if (new_num > (2**31 - 1)) or (new_num < -2**31):
            return 0
        else:
            return new_num
        

test_num = -1567890

my_test = Solution()
reverse_num = my_test.reverse(test_num)
print(reverse_num)
