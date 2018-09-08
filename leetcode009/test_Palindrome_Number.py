# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 进阶:
#
# 你能不将整数转为字符串来解决这个问题吗？


class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x % 10 == 0:
            return False
        else:
            new_num = 0
            while x > new_num:
                new_num = new_num * 10 + x % 10
                x = int(x / 10)

            return new_num == x or int(new_num / 10) == x


my_num = 1221

my_test = Solution()
result = my_test.isPalindrome(my_num)
print(result)

