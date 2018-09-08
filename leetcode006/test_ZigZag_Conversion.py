# 将字符串 "PAYPALISHIRING" 以Z字形排列成给定的行数：
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后从左往右，逐行读取字符："PAHNAPLSIIGYIR"
#
# 实现一个将字符串进行指定行数变换的函数:
#
# string convert(string s, int numRows);
# 示例 1:
#
# 输入: s = "PAYPALISHIRING", numRows = 3
# 输出: "PAHNAPLSIIGYIR"
# 示例 2:
#
# 输入: s = "PAYPALISHIRING", numRows = 4
# 输出: "PINALSIGYAHRPI"
# 解释:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution:
    def convert(self, s, numRows):
        len_s = len(s)
        if numRows >= len_s or numRows == 1:
            return s

        if numRows == 2:
            tmp_s1 = s[::2]
            tmp_s2 = s[1::2]
            return tmp_s1 + tmp_s2

        period = 2*numRows-2  # 求Z字形的周期
        new_str = str()

        for row_idx in range(numRows):
            if row_idx in [0, numRows-1]:
                tmp_s = s[row_idx::period]
            else:
                tmp_s = str()
                period_idx = 0
                while row_idx+period_idx*period < len_s:
                    tmp_s = tmp_s + s[row_idx+period_idx*period]
                    if period_idx*period+2*numRows-row_idx-2 < len_s:
                        tmp_s = tmp_s + s[period_idx*period+2*numRows-row_idx-2]

                    period_idx +=1

            new_str = new_str + tmp_s

        return new_str


list_string = ''

my_test = Solution()
convert_string = my_test.convert(list_string, 1)
print(convert_string)
