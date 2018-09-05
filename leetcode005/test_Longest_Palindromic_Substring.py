# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba"也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"

# 此题用动态规划来做，将已经搜索到的回文子串都标记为True
# 这样新的回文子串成立的判断条件就是中间的子串是回文子串，以及边上两个字符相等
class Solution:
    def longestPalindrome(self, s):

        len_string = len(s)
        palindromic_matrix = [[False for i in range(len_string)] for i in range(len_string)]
        len_max_substring = 0
        max_substring = ''
        for i_idx in range(len_string):
            j_idx = i_idx
            while j_idx >= 0:
                if i_idx == j_idx:  # 一个字符的情况
                    palindromic_matrix[i_idx][j_idx] = True
                    if i_idx-j_idx+1 > len_max_substring:
                        max_substring = s[j_idx:(i_idx+1)]
                        len_max_substring = i_idx-j_idx+1
                elif j_idx == i_idx - 1 and s[i_idx] == s[j_idx]:  # 相邻两个字符的情况
                    palindromic_matrix[i_idx][j_idx] = True
                    if i_idx-j_idx+1 > len_max_substring:
                        max_substring = s[j_idx:(i_idx+1)]
                        len_max_substring = i_idx-j_idx+1
                elif palindromic_matrix[i_idx-1][j_idx+1] is True and s[i_idx] == s[j_idx]:  # 相邻多个字符的情况
                    palindromic_matrix[i_idx][j_idx] = True
                    if i_idx-j_idx+1 > len_max_substring:
                        max_substring = s[j_idx:(i_idx+1)]
                        len_max_substring = i_idx-j_idx+1
                else:
                    pass

                j_idx = j_idx - 1

        return max_substring


list_string = 'woytehngwhattahwieyddtng'

my_test = Solution()
longest_string = my_test.longestPalindrome(list_string)
print(longest_string)
