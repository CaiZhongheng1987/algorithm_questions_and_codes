# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 两个字符串完全匹配才算匹配成功。
#
# 说明:
#
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 示例 1:
#
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 示例 2:
#
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 示例 3:
#
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 示例 4:
#
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 示例 5:
#
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输入: false


# 简化算法，用双指针进行匹配，s一个指针，p一个指针
# p = "c*ab*c"，可以匹配的s应该长成这样： "c....ab.....c"，省略号表示0到任意多的字符。
# 我们发现主要就是p的中间那个"ab"比较麻烦，一定要s中的'ab'来匹配，因此只要s中间存在一个"ab"，那么这两个*号之间的区域都认为匹配OK。
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is '':
            return p in ['', '*']

        if s is not '' and p is '':
            return False

        s_idx = 0
        p_idx = 0
        compare_begin = False
        store_p_idx = 0
        store_s_idx = 0
        len_s = len(s)
        len_p = len(p)

        while s_idx < len_s and p_idx < len_p:
            if p[p_idx] == '?':
                # 任意单个字符，肯定可以匹配上
                s_idx += 1
                p_idx += 1
            elif p[p_idx] == '*':
                # 遇到*号时的s_idx和p_idx+1要记录下来
                store_s_idx = s_idx
                p_idx += 1
                store_p_idx = p_idx
                compare_begin = True  # 说明从*号开始比较
            else:
                if p[p_idx] == s[s_idx]:
                    # 正常情况下两个字符比对上，各自的指针加上1
                    s_idx += 1
                    p_idx += 1
                elif compare_begin:
                    # 在当前不相等的情况下，如果前面出现了*号，那就说明可以将s往后挪，继续匹配
                    p_idx = store_p_idx
                    store_s_idx += 1
                    s_idx = store_s_idx
                else:
                    return False

        while p_idx < len_p and p[p_idx] == '*':
            # 这种情况适用于p的末尾还存在*的情况
            p_idx += 1

        if p_idx == len_p and s_idx == len_s:
            # 两者刚好匹配完全
            return True
        elif s_idx == len_s and p_idx < len_p:
            # s已经匹配完了，但是p还有剩且不为'*'，那肯定没匹配上
            return False
        elif '*' not in p:
            # 需要处理s = 'aa'， 而p = 'a'的匹配
            return False
        else:
            # 到这一步，就说明我们需要处理s = 'abcde'， 而p = '*c?'的匹配
            # 我们就从尾巴上重新开始回溯，进行判断
            s_end_idx = len_s - 1
            p_end_idx = len_p - 1
            while p[p_end_idx] != '*':
                if p[p_end_idx] in [s[s_end_idx], '?']:
                    p_end_idx -= 1
                    s_end_idx -= 1
                else:
                    break

            return p[p_end_idx] == '*'


s_string = "aa"
p_string = "a"

my_test = Solution()
result = my_test.isMatch(s_string, p_string)
print(result)
