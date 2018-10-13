# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
#
# 1. 1
#
# 2. 11
#
# 3. 21
#
# 4. 1211
#
# 5. 111221
#
# 1被读作"one 1"("一个一"), 即11。
#
# 11被读作"two 1s"("两个一"）, 即21。
#
# 21被读作"one 2", "one 1" （"一个二", "一个一"), 即1211。
#
# 给定一个正整数n（1 ≤ n ≤ 30），输出报数序列的第n项。
#
# 注意：整数顺序将表示为一个字符串。
#
#
# 示例
#
# 1:
#
# 输入: 1
#
# 输出: "1"
#
# 示例
#
# 2:
#
# 输入: 4
#
# 输出: "1211"


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'

        count_str = '1'
        for _ in range(2, n+1):
            acc_cnt = 0
            cur_count_str = ''
            len_str = len(count_str)
            str_flag = count_str[0]
            idx = 0
            while idx < len_str:
                if count_str[idx] == str_flag:
                    acc_cnt += 1
                else:
                    cur_count_str = cur_count_str + str(acc_cnt) + count_str[idx-1]
                    str_flag = count_str[idx]
                    acc_cnt = 1
                idx += 1

            # 到最后需要把最后一段相同的数字总结下来，添加到cur_cunt_str里面
            cur_count_str = cur_count_str + str(acc_cnt) + count_str[len_str - 1]
            count_str = cur_count_str

        return count_str


# main test script
test_num = 5

my_test = Solution()
out_str = my_test.countAndSay(test_num)
print(out_str)


