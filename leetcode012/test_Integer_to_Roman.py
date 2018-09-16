# 罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
# 给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
#
# 示例 1:
#
# 输入: 3
# 输出: "III"
# 示例 2:
#
# 输入: 4
# 输出: "IV"
# 示例 3:
#
# 输入: 9
# 输出: "IX"
# 示例 4:
#
# 输入: 58
# 输出: "LVIII"
# 解释: C = 100, L = 50, XXX = 30, III = 3.
# 示例 5:
#
# 输入: 1994
# 输出: "MCMXCIV"
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.


class Solution:
    def intToRoman(self, num):
        roman_dict = dict()
        roman_dict[1] = 'I'
        roman_dict[4] = 'IV'
        roman_dict[5] = 'V'
        roman_dict[9] = 'IX'
        roman_dict[10] = 'X'
        roman_dict[40] = 'XL'
        roman_dict[50] = 'L'
        roman_dict[90] = 'XC'
        roman_dict[100] = 'C'
        roman_dict[400] = 'CD'
        roman_dict[500] = 'D'
        roman_dict[900] = 'CM'
        roman_dict[1000] = 'M'

        roman_string = ''
        roman_list = list()
        tmp_num = num
        ten_num = 0
        while tmp_num > 0:
            list_val = list()
            tmp_val_10 = tmp_num % 10
            tmp_num = int(tmp_num / 10)
            if tmp_val_10 in [1, 2, 3]:
                for idx in range(tmp_val_10):
                    list_val.append(1)
            elif tmp_val_10 in [6, 7, 8]:
                list_val.append(5)
                for idx in range(tmp_val_10 - 5):
                    list_val.append(1)
            elif tmp_val_10 == 0:
                pass
            elif tmp_val_10 == 5:
                list_val = [5]
            elif tmp_val_10 == 4:
                list_val = [1, 5]
            else:
                list_val = [1, 10]

            list_val = [elem * (10**ten_num) for elem in list_val]
            ten_num += 1
            roman_list = list_val + roman_list

        for key in roman_list:
            roman_string = roman_string + roman_dict[key]

        return roman_string


dec_num = 8

my_test = Solution()
roman_string_out = my_test.intToRoman(dec_num)
print(roman_string_out)

