# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
# 说明:
#
# 所有输入只包含小写字母 a-z 。


class Solution:
    def longestCommonPrefix(self, strs):
        len_strs = len(strs)

        if len_strs == 0:
            return ''

        if len_strs == 1:
            return strs[0]

        if strs[0] == '':
            return strs[0]

        common_string = ''
        for p_idx in range(len(strs[0])):
            for c_idx in range(1, len_strs):
                if p_idx > len(strs[c_idx]) - 1:
                    return common_string

                if strs[0][p_idx] != strs[c_idx][p_idx]:
                    return common_string

            common_string = common_string + strs[0][p_idx]

        return common_string


test_list = ["c","c"]

my_test = Solution()
common_string_out = my_test.longestCommonPrefix(test_list)
print(common_string_out)
