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


# 采用动态规划来做通配符匹配，运行成功，但是超出时间限制
class Solution:
    def isMatch(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: bool
        """
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = (i == len(text))
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '?'}
                    if (not first_match) and pattern[j] is not '*':
                        ans = False
                    else:
                        if j < len(pattern) and pattern[j] == '*':
                            idx = i
                            ans = False
                            # 因为*代表任意字符，所以需要将text后面的字符都依次跳过去，和pattern匹配
                            while idx < len(text)+1:
                                ans = dp(idx, j+1)
                                if ans is True:
                                    # 说明匹配上了
                                    break
                                else:
                                    # 没匹配上的话，就继续挪动text中的一个字符，进行下一次匹配
                                    idx += 1
                        else:
                            ans = dp(i+1, j+1)

                memo[i, j] = ans

            return memo[i, j]

        return dp(0, 0)


s_string = "bbbbaaaaabaabbbbaabaaabaabbababbbaaabbababbbabaabaabaabababaaabaaaabbaabbaabbaaaaabbabbbbaaaababbaaaabbabbbaabaaabbaabaabaaababbabbaababaababbbbbaabbabbabbbbaabbaaababbabaaabbbbbbbbaababbbbbbabbaabaaa"
p_string = "b*a**b***abaabaaaba*abaaaaabaabb*bbb*aa*ab*a**b**b*a**a**a*abbb***bb*b*****baababaa**ab*aa*bbaba**bb*b*"

my_test = Solution()
result = my_test.isMatch(s_string, p_string)
print(result)
