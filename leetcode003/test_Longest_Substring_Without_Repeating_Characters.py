# 给定一个字符串，找出不含有重复字符的最长子串的长度。
#
# 示例：
#
# 给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。
#
# 给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。
#
# 给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。


class Solution:
    def lengthOfLongestSubstring(self, s):
        all_list = list(s)
        restore_dict = dict()
        max_len = 0
        left_idx = 0
        if s == '':
            max_len = 0
        else:
            for idx in range(0, len(all_list)):
                if all_list[idx] not in restore_dict.keys():
                    restore_dict[all_list[idx]] = idx
                else:
                    left_idx = max(restore_dict[all_list[idx]]+1, left_idx)
                    restore_dict[all_list[idx]] = idx

                max_len = max(max_len, idx-left_idx+1)

        return max_len


my_str = 'pwwkew'
my_test = Solution()
max_len_out = Solution.lengthOfLongestSubstring(my_test, my_str)
print(max_len_out)
